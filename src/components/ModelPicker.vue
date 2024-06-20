<template>
        <div class="gpt-model-choice-container">
            <h2>{{ this.model }}</h2>
            <DropDown />
        </div>
</template>

<script>
import DropDown from "./DropDown.vue"
export default {
    name: "ModelPicker",
    components: {
        DropDown
    },
    props: ["model"]
}
</script>

<style>
.gpt-model-choice-container {
    width: 18%;
    height: 40%;
    /*border: solid 1px grey;*/
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
</style>
