<template>
  <div class="bg-dark h-screen">
    <div class = "flex" style="height: 88vh;">
      <!-- side navigation-->
      <div class = "w-56 bg-black h-full flex-none">
        <div class="p-4">
          <img src = "images/moodifyLogo.png" class="h-10" style="filter: brightness(1) invert(1);">
        </div>
        <div class ="mx-2">
          <button class ="'w-full text-xs rounded px-3 py-2 flex items-center justify-start">
          </button>
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
          const res = await fetch('http://localhost:5000/playlists', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(playlist),
          })
          const data = await res.json()
          this.playlists = [...this.playlists, data]
      },
      async fetchPlaylists() {
          const res = await fetch('http://localhost:5000/playlists');

          const data = await res.json();
          return data;
      }
  },
  async created() {
      this.playlists = await this.fetchPlaylists();
  }
}
</script> 