<template>
    <div class="io-head-container">
        <h2 class="input-lang-display">{{this.name}}</h2>  
        <DropDown />
    <input type="file" id="file-input" @change="this.handleFileInput($event)"/>
    </div>
    <input type="text" id="text-input-box" class="code-input-box"/>
</template>

<script>
    import DropDown from "../components/DropDown.vue";
    import pako from 'pako';
    import Buffer from 'buffer';

    export default {
        name:"InputForm",
        props: ["name", "email"],
        components: {
            DropDown,
        },
        data(){
            let contents = null;
            const email = this.email;
        },
        methods: {
            handleFileInput(e){
                const fileHolder = e.target.files;
                console.log(fileHolder) 
                switch (fileHolder.length){
                    case 0:
                        console.log("No file selected");
                        break;
                    case 1:
                        console.log("Hit case 1");
                        let reader = new FileReader();
                        const file = fileHolder[0];
                        reader.onload = (e) => { //This is the only thing that is performing an 
                            console.log(e.target.result); // operation on the contents of the file 
                            this.contents = this.compressFile(e.target.result);
                            this.sendFile();
                        };
                        reader.onerror = (e) => {
                            console.error("Error reading file.", e.target.error);
                        };
                        reader.readAsText(file); //This activates the onload callback once the file is read.
                        break;
                    default:
                        console.log("too many files selected");
                }
            },// END OF handleFileInput
            uint8ToBase64(uint8) {
                return btoa(String.fromCharCode.apply(null, uint8));
            },
            compressFile(fileContents){
                let compressed = pako.deflate(fileContents); // Function to compress and encode a string
                let base64String = this.uint8ToBase64(compressed);
                const b64Split = base64String.split('');
                for (let i = 0; i < b64Split.length; i++){
                    if (b64Split[i] == "/") {
                        console.log(b64Split[i], i);
                        b64Split[i] = "+";
                    }
                }
                const final = b64Split.join('');
                console.log("Compressed and encoded string:", base64String);
                return final;

            },// END OF CompressFile
            async sendFile() {
                console.log("Attempting to send file to API");
                try{
                    let dataToSend = this.contents;
                    let response = await fetch(`http://localhost:5000/api/core/rec_file/${this.email}/${dataToSend}`);
                    if (!response.ok) throw new Error("Server did not respond with OK");
                    let result = await response.json();
                    console.log("Operation SendFile was a ", result);
                }catch(err){
                    console.log(err);
                }finally{
                    console.log("No longer Loading");
                }
            },//END OF sendFile
        }
    }

</script>

<style>

.input-lang-display{
    color: black;
    font-weight: 500;
    font-size: 16pt;
    text-align: center;
}

.io-head-container {
    width: 100%;
    height: 10%;
    /*border: solid 1px grey;*/
    display: flex;
    align-items: center;
    gap: 5%;
}

.code-input-box {
    border: solid 1px;
    border-color: #DDDDDD;
    border-radius: 1%;
    height: 90%;
    width: 90%;
    text-align: center;
}

</style>

