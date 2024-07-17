<script>
    import Showcase from "./layouts/Showcase.vue"
    import NavBar from "./layouts/NavBar.vue"
    //import Login from "./layouts/Login.vue"

    export default {
        name: "App",
        components: {
            NavBar,
            Showcase,
        },
        methods: {
        },
    }

</script>

<template>
    <NavBar/>
    <Showcase/>
</template>

<style>
#app{
    display: flex;
    flex-direction: column;
}
</style>
