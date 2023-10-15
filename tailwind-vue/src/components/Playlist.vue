<template>
    <div class="playlist">
        <h3>{{ playlist.id }}</h3>
        <h3>{{ playlist.playlist }}</h3>
    </div>
</template>

<script>
    export default {
        name: 'Playlist',
        props: {
            playlist: Object
        }
    }
</script>