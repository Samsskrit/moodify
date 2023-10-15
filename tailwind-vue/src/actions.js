import { initializeApp } from "firebase/app";
import {
  getDatabase,
  ref,
  set,
  onValue,
  query,
  orderByChild,
  limitToLast,
} from "firebase/database";
import { getAuth, signInAnonymously } from "firebase/auth";
import { firebaseConfig } from "../../firebase.config.js";

let initial = true;

function auth() {
  const auth = getAuth();
  const user = auth.currentUser
  if (user) {
    console.log('sheeesh', user)
  } else {
    console.log('wtf')
  }
  alert('wtfff')
  let p = new Promise(function (resolve, reject) {
    signInAnonymously(auth)
      .then(() => {
        resolve(true);
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        console.log(errorCode);
        console.log(errorMessage);
        reject(false);
      });
  });
  return p;
}

export async function writeUserData(userId, base64) {
  // Initialize Firebase
  const app = initializeApp(firebaseConfig);

//   let result = await auth();
//   if (!result) return;

  // Initialize Realtime Database and get a reference to the service
  const db = getDatabase();
  console.log(db)
  console.log(ref(db, "moods/"))
  await moodListener(1)
  set(ref(db, "images/" + "image_" + userId), { image: base64 });
}

export async function moodListener(accessToken) {
//   let result = await auth();
//   if (!result) return;
  const db = getDatabase();
  const moodRef = db.ref(db, "moods/");
  console.log(moodRef)
  onValue(moodRef, (snapshot) => {
    const data = snapshot.val();
    console.log(data)
  });
}

async function actions(accessToken, data) {
  if (initial) {
    initial = false;
    return;
  }
  console.log(data);

  const result = await createPlaylist(accessToken);
  console.log("Create Playlist");
  console.log(result);

  const result2 = await fetchSongs(
    accessToken,
    Object.values(data)[Object.values(data).length - 1].genres
  );
  console.log("Fetch Songs");
  console.log(Object.values(data)[Object.values(data).length - 1].genres);
  console.log(result2);

  const result3 = await addPlaylistSongs(accessToken, result, result2);
  console.log(result3);

  populatePlaylist(result);

  //insert into database
  writeUserData(Object.values(data).length, result.uri);
}