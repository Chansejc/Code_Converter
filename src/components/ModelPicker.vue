<template>
        <div id="gpt-model-choice-container">
            <h2 id="model-title">{{ this.model }}</h2>
            <input type="submit" id="convert-button" 
                value="Convert" @click="this.sendPayload"></input>
        </div>
</template>

<script>
import pako from 'pako';
export default {
    name: "ModelPicker",
    components: { },
    props: ["model"],
    methods: {
        getInput(){
            let inputBox = document.getElementById("code-input-box");
            let value = inputBox.value; 
            return value;
        }, // END 
        uint8ToBase64(uint8) {
            return btoa(String.fromCharCode.apply(null, uint8));
        },// END 
        compressPayload(){
            let compressed = pako.deflate( this.preMinimized() ); // Function to compress and encode a string
            console.log("After deflating" , compressed);
            console.log(btoa(String.fromCharCode.apply(null, compressed)));
            let payload = this.uint8ToBase64(compressed);
            return payload

        },// END
        async sendPayload() {
            try{
                let langContainers = document.getElementsByClassName("dropbtn");
                let inputLang = langContainers[0].innerText;
                let outputLang = langContainers[1].innerText;

                console.log("Language", inputLang);
                console.log("Language", outputLang);
                let payload = await this.compressPayload();
                let response = await fetch(`http://localhost:5000/api/core/send_payload/`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({"data": { "payload": payload, "InputLanguage": inputLang, "OutputLanguage": outputLang } })
                });

                if (!response.ok) throw new Error("Server did not respond with OK");
                let result = await response.json();
                let outputBox = document.getElementById("code-output-box");
                outputBox.value = await result.data;
                console.log("Operation SendFile was a ", result);
            }catch(err){
                console.log(err);
            }finally{
                console.log("No longer Loading");
            }
        },//END 
        preMinimized(){
            let smallValue = document.getElementById("code-input-box").value.replace(/(\r\n)/gm, "%rn");
            smallValue = smallValue.replace(/(\n)/gm, "%n");
            smallValue = smallValue.replace(/(\r)/gm, "%r");
            smallValue = smallValue.replace(/(\t)/gm, "%t");
            smallValue = smallValue.replace(/( )/gm, "%sp");
            console.log(smallValue); // \r\n|\n|\r|\t
            return smallValue;
        },
    }
}
</script>

<style>
#gpt-model-choice-container {
    width: 18%;
    height: 40%;
    /*border: solid 1px grey;*/
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
}
#gpt-model-choice-container > *{
    /*border: solid 1px green;*/
    margin: 0;
}

#model-title{

}

#convert-button{
    height: 45px;
    width: 100px;
    font-weight: 600;
    font-size: 14pt;
    border-radius: 5px;
    background: none;
    border: none;
    box-shadow: 1px 2px 2px 3px rgba(0,0,0,0.1);
}

</style>
