<template>
    <div class="io-head-container">
        <h2 class="input-lang-display">{{this.name}}</h2>  
        <DropDown />
    </div>
    <input type="file" id="file-input"/>
    <input type="text" id="text-input-box" class="code-input-box"/>
</template>

<script>
import DropDown from "../components/DropDown.vue"
export default {
    name:"InputForm",
    props: ["name"],
    components: {
        DropDown,
    },
    methods: {
        readInputContents(){
            document.getElementById('file-input').addEventListener('change', function(event) {
                const fileHolder = event.target.files;
                console.log(fileHolder) 
                if (fileHolder.length > 1) {
                    for(let i = 0; i < fileHolder.length; i++){
                        let file = fileHolder[i];

                        if (file) {
                            const reader = new FileReader();
                            
                            reader.onload = function(e) {
                                const contents = e.target.result;
                                console.log(contents); // Process the contents here
                            };
                            
                            reader.onerror = function(e) {
                                console.error("Error reading file:", e.target.error);
                            };

                            reader.readAsText(file); // Read the file as text
                        } else {
                            console.log("No file selected");
                        }

                    }
                }
            }); 
        },// END OF readInputContents
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

