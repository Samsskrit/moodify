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
    <Header title="ww"/>
    <Form />
  </div>
  
</template>

<script>
import Header from './components/Header.vue'
import Form from './components/UploadForm.vue'
export default {
  name: 'App',
  /*data: function() {
    return {
      pages: [
        {id: 'home', name: 'Home', icon:"home"},
        {id: 'library', name: 'Your Library', icon:"library_music"},
      ]
    };
  },*/
  components: {
      Header,
      Form
  },
}
</script> 