<template>
    <div id="i-head-container">
        <h2 id="input-lang-display">{{this.name}}</h2>  
        <DropDown :opts="this.languages" />
    </div>
    <textarea id="code-input-box" maxlength="800" value="Type here"
            @input="e => this.getChars(e)"></textarea> 

    <h2 id="char-counter">{{this.currentChars}} / {{this.MAXCHARS}}</h2>
</template>
<script>
    import DropDown from "../components/DropDown.vue";
    const MAXCHARS = 800;
    let inputBox =  document.getElementById("code-input-box");
    let currentChars = 0;
    let lastPressed = null;
    const languages = [
        { name: "Python" },
        { name: "C++"},
        { name: "C"},
        { name: "Go"},
        { name: "Rust"},
        { name: "Elixr"},
        { name: "Lua"},
        { name: "TypeScript"},
        { name: "Java"}
    ];

    export default {
        components: {
            DropDown
        },
        data() {
            return {
                languages,
                currentChars,
                MAXCHARS
            }
        },  
        methods: {
            getChars(event){ //This is constantly changing the character counter element
                let curValue = event.target.value;
                let cur = (this.inputBox !== null) ? curValue.length : 0;
                this.currentChars = cur;
            },//end of this.getChars
        },
        props: [
            'name'
        ],
    }
</script>

<style>

#input-lang-display{
    color: black;
    font-weight: 600;
    font-size: 16pt;
    text-align: center;
}

#i-head-container {
    width: 100%;
    height: 10%;
    /*border: solid 1px grey;*/
    display: flex;
    align-items: center;
    gap: 5%;
}

#code-input-box {
    border: solid 1px;
    border-color: #DDDDDD;
    border-radius: 1%;
    height: 85vh;
    width: 35vw;
    text-align: start;
}

textarea {
  width: 100%;
  padding: 12px 20px;
  box-sizing: border-box;
  /*border: 2px solid #ccc;*/
  border-radius: 4px;
  background-color: #f8f8f8;
  font-size: 14pt;
  resize: none;
}

</style>

