<template>
    <div class="profileitem-container">
        <img src="../assets/rai_picture.jfif" alt="Some image"/>
    </div>
</template>

<script>
export default {
    name: "ProfileItem",
    created(){
        console.log(this.image);
    }
}
</script>

<style scoped>
.profileitem-container {
    border: solid;
    border-radius: 50%;
    height: 50px;
    width: 50px;
}
img {
    height: 50px;
    width: 50px;
    border-radius: 50%;
}
</style>
