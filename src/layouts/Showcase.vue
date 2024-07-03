<template>
    <div class="showcase-container">
        <div class="input-form-container">
            <InputForm email=cc@buchanan.com name=Python />
        </div>
        <ModelPicker model="GPT-4" />
        <div class="output-form-container">
            <OutputForm name=C# />
        </div>
    </div>
</template>

<script>
import InputForm from "../layouts/InputForm.vue"
import OutputForm from "../layouts/OutputForm.vue"
import ModelPicker from "../components/ModelPicker.vue"
export default{
    name:"Showcase",
    components: {
        InputForm,
        OutputForm,
        ModelPicker
    }
}
</script>

<style>
.showcase-container {
    /*border: solid 1px grey;*/
    height: 80vh;
    width: 100%;
    display: flex;
    align-items: center;
}
.input-form-container, .output-form-container{
    /*border: solid 1px grey;*/
    height: 100%;
    width: 40%;
    display:flex;
    flex-direction: column;
    justify-content: space-between;
    margin-left: 2.5%;
    margin-right: 2.5%;
}
</style>
