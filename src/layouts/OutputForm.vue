<template>
    <div id="o-head-container">
        <h2 id="output-lang-display">{{this.name}}</h2>  
        <DropDown v-bind:opts="this.languages" />
    </div>
    <textarea id="code-output-box" ></textarea>
</template>

<script>
import DropDown from "../components/DropDown.vue"
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
    name:"OutputForm",
    props: ["name"],
    components: {
        DropDown,
    },
    data(){
        return{
            languages
        }
    }
}
</script>

<style>
#output-lang-display{
    color: black;
    font-weight: 600;
    font-size: 16pt;
    text-align: center;
}

#o-head-container {
    width: 100%;
    height: 10%;
    /*border: solid 1px grey;*/
    display: flex;
    align-items: center;
}

#code-output-box {
    border: solid 1px;
    border-color: #DDDDDD;
    border-radius: 1%;
    height: 90%;
    width: 90%;
    text-align: start;
}

</style>
