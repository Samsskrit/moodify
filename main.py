import firebase_admin
from firebase_admin import db, credentials, auth
from detect_emotion import DetectEmotion

DetectEmotion = DetectEmotion()
cred = credentials.Certificate("C:\\Users\\samue\\Documents\\GitHub\\moodify\\firebase.config.js")
firebase_admin.initialize_app(cred)
db = firebase_admin.db()

base64_ref = db.reference("images/")
mood_list_ref = db.reference("moods/")

def auth():
    try:
        auth.sign_in_anonymous()
        return True
    except auth.AuthError as e:
        error_code = e.code
        error_message = e.message
        print("Error code: {0}".format(error_code))
        print("Error message: {0}".format(error_message))
        return False

async def write_moods_to_firebase(user_id):
    result = await auth()

    if not result:
        return

    base64_str, size = await read_base64_from_firebase(user_id)
    genre_mood_list = DetectEmotion.get_genre_by_emotion(base64_str)
    mood = genre_mood_list[-1]
    genre_list = genre_mood_list[:-1]

    # size of moods_branch will always be size
    moods_branch = mood_list_ref.get()
    moods_branch.set({
        "mood_{}".format(size): {
            "genres": genre_list,
            "mood": mood,
        }
    })


async def read_base64_from_firebase(user_id):
    result = await auth()

    if not result:
        return

    base64_branch = base64_ref.get()
    size = len(base64_branch)

    base64_str = base64_ref.order_by_key().limit_to_last(1).get()
    # event_listener = base64_ref.listen(update_list)
    return base64_str, size

def update_list(event):
    base64_data = event.data
    if base64_data:
        genre_list = DetectEmotion.get_genre_by_emotion(base64_data)
        print(genre_list)
        mood_list_ref.set(genre_list)
