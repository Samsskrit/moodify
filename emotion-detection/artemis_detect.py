import torch
from PIL import Image
from torchvision import transforms
import numpy as np
import pandas as pd
from ast import literal_eval
import argparse

from artemis.neural_models.image_emotion_clf import ImageEmotionClassifier
from artemis.neural_models.resnet_encoder import ResnetEncoder
from artemis.neural_models.mlp import MLP
from artemis.neural_models.image_emotion_clf import evaluate_on_dataset
from artemis.in_out.neural_net_oriented import torch_load_model, torch_save_model, image_emotion_distribution_df_to_pytorch_dataset
from artemis import emotions


# Load saved histograms of emotion choices as computed with "previous" notebook (see top-README if you are lost)
# image_hists_file = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\data\\image-emotion-histogram.csv"
# image_hists = pd.read_csv(image_hists_file)

# # this literal_eval brings the saved string to its corresponding native (list) type
# image_hists.emotion_histogram = image_hists.emotion_histogram.apply(literal_eval)

# # normalize the histograms
# image_hists.emotion_histogram = image_hists.emotion_histogram.apply(lambda x: (np.array(x) / float(sum(x))).astype('float32'))

# print(f'Histograms corresponding to {len(image_hists)} images')

#---------------------------------------------
# artemis_data = pd.read_csv("C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\data_out\\preprocessed_data.csv")
# artemis_data = artemis_data.drop_duplicates(subset=['art_style', 'painting'])
# artemis_data.reset_index(inplace=True, drop=True)

# artemis_data = artemis_data[['art_style', 'painting', 'split']] 

# artemis_data.head()
# image_hists.head()

# artemis_data = artemis_data.merge(image_hists)
# artemis_data = artemis_data.rename(columns={'emotion_histogram': 'emotion_distribution'})

# n_emotions = len(image_hists.emotion_histogram[0])
# print('Using {} emotion-classes.'.format(n_emotions))
# assert all(image_hists.emotion_histogram.apply(len) == n_emotions)
n_emotions = len(emotions.ARTEMIS_EMOTIONS)
# print(n_emotions)

pt_model_path = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\best_model.pt"

# prepare data
# artemis_data = pd.read_csv(osp)


# create device for running the model
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
criteria = torch.nn.KLDivLoss(reduction='batchmean').to(device)

# img encoding
img_encoder = ResnetEncoder('resnet34', adapt_image_size=1, pretrained=True).unfreeze(level=7, verbose=True)
img_emb_dim = img_encoder.embedding_dimension();

# make MLP 
clf_head = MLP(img_emb_dim, [100, n_emotions], dropout_rate=0.3, b_norm=True, closure=torch.nn.Softmax(dim=-1))
# load the model
model = ImageEmotionClassifier(img_encoder, clf_head).to(device)
optimizer = torch.optim.Adam([{'params': filter(lambda p: p.requires_grad, model.parameters()), 'lr': 5e-4}])

# load the model
model = torch_load_model(pt_model_path)
model = model.to(device)
# test_loss, test_confidence = evaluate_on_dataset(model, data_loaders['test'], criteria, device)
# model.load_state_dict(torch.load(pt_model_path, map_location=device))
# model.eval()

# load the image
# img_path = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\images\\starrynight.jpg"
img_path = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\images\\dude_and_girl.jpg"
img = Image.open(img_path)
img = transforms.ToTensor()(img)
img = img.unsqueeze(0)
img = img.to(device)

# pass the image through the model
with torch.no_grad():
    output = model(img)

# get the emotion
output = output.cpu().numpy()
print(output)
emotion = np.argmax(output)
# emotion = np.argmax(output, dim=1)
print(emotion)

emotions = emotions.ARTEMIS_EMOTIONS
print(emotions[emotion])

