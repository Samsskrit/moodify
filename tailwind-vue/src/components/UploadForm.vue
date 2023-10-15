<template>
    <form @submit="onSubmit()">
        <input id="uploadImage" type="file" ref="file" @change="handleFileUpload($event)" required/>
        <img id="preview" src="#" alt="uploaded image">
        <!-- <input type="submit" value="Upload Image"/> -->
        <button @click="onSubmit()">SUBMIT</button>
    </form>
</template>

<script>

    let base64String = '';
    let blobString = '';

    export default {
        name: 'Form',
        data() {
            return {
                imageLink: '',
                playlist: '',
            }
        },
        methods: {
            handleFileUpload ($event) {
                console.log(event.target.files[0])
                this.file = event.target.files[0]

                if (this.file) {
                    preview.src = URL.createObjectURL(this.file);

                    const reader = new FileReader();
                    reader.onload = function () {
                        base64String = reader.result.replace("data:", "")
                            .replace(/^.+,/, "");
                    };
                    reader.readAsDataURL(this.file);
                }
            },
            onSubmit(e) {
                const newPlaylist = {
                    'img_base64': base64String
                }
                this.$emit('upload', newPlaylist)

                this.file = ''
            }
        }
    }
</script>