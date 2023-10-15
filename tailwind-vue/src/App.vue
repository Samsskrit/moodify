<template>
  <div class="bg-dark h-screen">
    <div class = "flex" style="height: 88vh;">
      <!-- side navigation-->
      <div class = "w-60 bg-black h-full flex-none">
        <div class="p-5">
          <div>
            <img src = "images/moodifyLogo.png" class="h-10" style="filter: brightness(1) invert(1);">
            <body text="white" style="font-family:cursive"  > 
            <p style="font-size:xxx-large">Moodify </p>
            </body>
          </div>
        </div>
        <div class ="h-px w-full bg-light my-3"> </div>
        <div class ="mx-2 mb-7">
          <button class ="'w-full text-xs rounded px-3 py-2 flex items-center justify-start">
            <img src = "images/home.png" class="h-9" style="filter: brightness(0) invert(1);">
            <body text="white" style="font-family:cursive;"  > 
            <p style="font-size:large">&nbsp &nbsp Home </p>
            </body>
          </button>
          <br>
          <button class ="'w-full text-xs rounded px-3 py-2 flex items-center justify-start">
            <img src = "images/library.png" class="h-9" style="filter: brightness(0) invert(1);">
            <body text="white" style="font-family:cursive;"  > 
            <p style="font-size:large">&nbsp &nbsp Your Library </p>
            </body>
          </button>
        </div>
        <div class ="h-px w-full bg-light my-3"> </div>
        <div class = "mx-5">  
            <h1 class ="text-xs text-lightest tracking-widest uppercase"> Playlists</h1> <br>
            <button type="file" class ="flex items-center justify-start">
              <img src="images/add.png" class ="h-8 w-8 mr-3" style="filter: brightness(0) invert(1);"/>
              <body text="white" style="font-family:cursive;"  > 
                <p style="font-size:large">Create Mood Mix </p>
              </body>
            </button> 
        </div>

        <div class ="h-px w-full bg-light my-3"> 
          <form @submit="onSubmit()">
            <input id="uploadImage" type="file" @change="displayImage()" required/>
            <input type="submit" value="Upload Image"/>
          </form>
        </div>

      </div>

      <!-- main content-->
      <div class="w-full h-full relative">
        <!-- header -->
        <div class="w-full sticky top-0 p-2">
        </div>
      </div>
    </div>
    <!--play bar-->
    <div class="w-full bg-light" style="height: 12vh;">

    </div>
    <div>
        <Header title="ww"/>
        <Form @upload="addNewPlaylist"/>
        <Playlists :playlists="playlists" />
    </div>
  </div>
  
</template>

<script>
import Header from './components/Header.vue'
import Form from './components/UploadForm.vue'
import Playlists from './components/Playlists.vue'
import { writeUserData, moodListener } from './actions.js'
export default {
  name: 'App',
  data() {
      return {
          playlists: []
      }
  }, 
  components: {
      Header,
      Form,
      Playlists
  },
  methods: {
      async addNewPlaylist(playlist) {
        console.log(playlist)
        alert('a')
        // let writeToIndex = await readIndices();  
        // await writeUserData(1, playlist);
        moodListener(1)
      },
      async fetchPlaylists() {
          // const res = await fetch('http://localhost:5000/playlists');

          // const data = await res.json();
          // return data;
      }
  },
  async created() {
      this.playlists = await this.fetchPlaylists();
  }
}
</script> 