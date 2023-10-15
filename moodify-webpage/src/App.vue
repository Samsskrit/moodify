<template>
    <div>
        <Header title="ww"/>
        <Form @upload="addNewPlaylist"/>
        <Playlists :playlists="playlists" />
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
            console.log(playlist)
            alert('stop')
            const res = await fetch('http://localhost:5000/playlists', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(playlist),
            })
            console.log(playlist)
            alert('stop')
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