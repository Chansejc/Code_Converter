<template>
    <div class="nav-container">
        <p>Code Converter</p> 
        <div class="right-item-container">
            <NavItemSmall title="Share"/>
            <ProfileItem />
        </div>
    </div>
</template>

<script>
import NavItemSmall from "../components/NavItemSmall.vue"
import ProfileItem from "../components/ProfileItem.vue"
export default {
    name: "NavBar",
    components:{
        NavItemSmall,
        ProfileItem
    },
}

</script>

<style>
.nav-container {
   width: 100%;
   height: 75px;
   border-bottom: solid grey 1px;
   background: white;
   display: flex;
   justify-content: space-between;
   align-items: center;
}
.right-item-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-right: 2rem;
    width: 150px;
}
p {
    margin: 1rem 2rem;
    font-size: 20pt;
    font-weight: 600;
}
</style>
