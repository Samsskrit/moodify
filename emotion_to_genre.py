from detect_emotion import DetectEmotion

DetectEmotion = DetectEmotion()
model = DetectEmotion.load_model()

# !TODO: fetch and decode base64 image
img_path = "C:\\Users\\samue\\Documents\\GitHub\\artemis\\artemis\\images\\starrynight.jpg"
img = DetectEmotion.load_image(img_path)

# !TODO: give emotion as output to backend
emotion = DetectEmotion.detect_emotion(img, model)
genres = DetectEmotion.get_genre_by_emotion(emotion)
