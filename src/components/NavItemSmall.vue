<template>
    <div class="navitem-container-small">
        <p>{{this.title}}</p>
    </div>
</template>

<script>
export default {
    name: "NavItemSmall",
    props: ['title'],
    methods: {},
    created() {},
}
</script>

<style>
.navitem-container-small{
    margin-right: 1rem;
    border-radius: 15px;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    /*box-shadow: 4px 6px 0px rgb(0, 0, 0, 2);*/
}
p {
    font-size: 12pt;
    font-weight: 400;
    margin: 1rem;
}
</style>
