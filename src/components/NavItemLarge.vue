<template>    
    <div class="navitem-container-large">
        <p>{{this.title}}</p>
    </div>
</template>

<script>
export default {
    name: "NavItemLarge",
    props: ["title"],
    methods: {},
    oncreated(){}
}
</script>

<style>
.navitem-container-large{
    /*margin-right: 1rem;*/
    border-top: solid 1px grey;
    background: white;
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
