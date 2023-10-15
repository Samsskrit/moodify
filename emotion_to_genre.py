from detect_emotion import DetectEmotion
from thing import Base64
import base64

DetectEmotion = DetectEmotion()

# !TODO: fetch and decode base64 image
genre_list = DetectEmotion.get_genre_by_emotion(Base64)
print(genre_list)

# !TODO: give dict as output to backend