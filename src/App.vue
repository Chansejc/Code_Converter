<script>
    import Showcase from "./layouts/Showcase.vue"
    import NavBar from "./layouts/NavBar.vue"
    import Footer from "./layouts/Footer.vue"
    import Login from "./layouts/Login.vue"

    export default {
        name: "App",
        components: {
            NavBar,
            Showcase,
            Footer,
            Login
        }
    }
</script>

<template>
    <Login />
</template>

<style>
</style>
