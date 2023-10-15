<template>
    <form @submit="onSubmit()">
      <div class = "center">
        <button type="file" class ="flex items-center justify-start">
            <img src="images/add.png" class ="h-8 w-8 mr-3" style="filter: brightness(0) invert(1);"/>
              <body text="white" style="font-family:cursive;">
                <p style="font-size:large">
                  <label for="uploadImage">
                    Create Mood Mix
                  </label>
                </p>
              </body>
              <input id="uploadImage" type="file" ref="file" @change="handleFileUpload($event)" required/>
        </button> <br>
        <input id = "submitBtn" type="submit" value="I'm happy with this image!"/>
      </div>
      <img id="preview" src="#" alt="uploaded image">
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
<style scoped>
label {
   cursor: pointer;
   color: white;
   top: 50%;
   font-size: 50px;
   text-decoration:underline;
}

#uploadImage {
   opacity: 0;
   position: absolute;
   z-index: -1;
}

#submitBtn {
    cursor: pointer;
    font-family: cursive;
    color: white;
    border: 2px solid whitesmoke;
    background-color: grey;
    position: absolute;
    width: 450px;
}

#preview {
    color: grey;
    object-fit: cover;
    display: block;
    max-width:400px;
    max-height:400px;
    width: auto;
    height: auto;
    position: absolute;
    top: 40%;
    right: 35%;
}

.center {
    position: absolute;
    top: 20%;
    left: 32%;
}
</style>