import torch
from PIL import Image
from torchvision import transforms
import numpy as np
# import pandas as pd
# from ast import literal_eval
# import argparse

from artemis.neural_models.image_emotion_clf import ImageEmotionClassifier
from artemis.neural_models.resnet_encoder import ResnetEncoder
from artemis.neural_models.mlp import MLP
from artemis.neural_models.image_emotion_clf import evaluate_on_dataset
from artemis.in_out.neural_net_oriented import torch_load_model, torch_save_model, image_emotion_distribution_df_to_pytorch_dataset
from artemis import emotions
from genres import GenreId

class DetectEmotion():
    def __init__(self) -> None:
        self.emotions = emotions.ARTEMIS_EMOTIONS
        self.n_emotions = len(self.emotions)
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.criteria = torch.nn.KLDivLoss(reduction='batchmean').to(self.device)
        self.pt_model_path = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\best_model.pt"

    def img_encoding(self) -> list:
        img_encoder = ResnetEncoder('resnet34', adapt_image_size=1, pretrained=True).unfreeze(level=7, verbose=True)
        img_emb_dim = img_encoder.embedding_dimension();
        return [img_encoder, img_emb_dim]

    def load_model(self) -> ImageEmotionClassifier:
        [img_encoder, img_emb_dim] = self.img_encoding()
        clf_head = MLP(img_emb_dim, [100, self.n_emotions], dropout_rate=0.3, b_norm=True, closure=torch.nn.Softmax(dim=-1))
        model = ImageEmotionClassifier(img_encoder, clf_head).to(self.device)
        # optimizer = torch.optim.Adam([{'params': filter(lambda p: p.requires_grad, model.parameters()), 'lr': 5e-4}])
        model = torch_load_model(self.pt_model_path)
        model = model.to(self.device)
        model.eval()
        return model

    def load_image(self, img_path) -> Image:
        img_path = img_path
        img = Image.open(img_path)
        img = transforms.ToTensor()(img)
        img = img.unsqueeze(0)
        img = img.to(self.device)
        return img

    def detect_emotion(self, img, model) -> str:
        with torch.no_grad():
            output = model(img)
        output = output.cpu().numpy()
        emotion = np.argmax(output)
        return self.emotions[emotion]

    def get_genre_by_emotion(self, emotion) -> list:
        genre_names = []
        for genre in GenreId.items():
            if genre[1]["emotion"] == emotion:
                genre_names.append(genre[1]["name"])
        return genre_names
