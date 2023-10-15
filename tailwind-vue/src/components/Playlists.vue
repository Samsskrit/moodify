<template>
    <div v-for="playlist in playlists">
        <Playlist :playlist="playlist" />
    </div>
</template>

<script>
import Playlist from './Playlist.vue'
    export default {
        name: 'Playlists',
        props: {
            playlists: Array
        },
        components: {
            Playlist,
        }
    }
</script>