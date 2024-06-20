<template>
    <div class="io-head-container">
        <h2 class="output-lang-display">{{this.name}}</h2>  
        <DropDown />
    </div>
    <input type="text" class="code-input-box"/>
</template>

<script>
import DropDown from "../components/DropDown.vue"
export default {
    name:"OutputForm",
    props: ["name"],
    components: {
        DropDown,
    }
}
</script>

<style>
.output-lang-display{
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
