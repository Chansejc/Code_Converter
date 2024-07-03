<template>
    <div class="navitem-container-small">
        <button id="share" onclick="this.copyLink">{{this.title}}</button>
    </div>
</template>

<script>
export default {
    name: "NavItemSmall",
    props: ['title'],
    created() {
            
    },
    methods: {
        copyLink() {
            var temp = $("<input>");
            $("body").append(temp);
            temp.value = "code-converter.com";
            document.select(temp);
            document.execCommand("copy");
            temp.remove();
        },
    },

}
</script>

<style>

.navitem-container-small {
    margin-right: 1rem;
    border-radius: 15px;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    box-shadow: 4px 6px 0px rgb(0, 0, 0, .1);
}
.navitem-container-small > button {
    font-size: 12pt;
    font-weight: 400;
    margin: 1rem;
}

</style>
