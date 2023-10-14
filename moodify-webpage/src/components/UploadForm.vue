<template>
    <form @submit="onSubmit()">
        <input id="uploadImage" type="file" @change="displayImage()" required/>
        <img id="preview" src="#" alt="uploaded image">
        <input type="submit" value="Upload Image"/>
    </form>
</template>

<script>
    export default {
        name: 'Form',
        methods: {
            displayImage() {
                console.log(uploadImage.files);
                const [file] = uploadImage.files;
                if (file) {
                    preview.src = URL.createObjectURL(file);
                }
            },
            onSubmit(e) {
                console.log("hiii");
                e.preventDefault();

            }
        }
    }
</script>