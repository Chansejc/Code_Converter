<template>
    <div id="slogan-main-container">
        <div id="block-1-container">
            <div id="block-1-spacer"></div>
            <img class="slogan-icon" src="../components/icons/Edit.png">
            <h2 class="slogan-text">Language</h2>
        </div>
        <div id="block-2-container">
            <div id="block-2-spacer"></div>
            <img class="slogan-icon" src="../components/icons/cancel (1).png">
            <h2 class="slogan-text">Shouldn't</h2>
        </div>
        <div id="block-3-container">
            <div id="block-3-spacer"></div>
            <img class="slogan-icon" src="../components/icons/error.png">
            <h2 class="slogan-text">Hinder</h2>
        </div>
        <div id="block-4-container">
            <div id="block-4-spacer"></div>
            <img class="slogan-icon" src="../components/icons/Cpu.png">
            <h2 class="slogan-text">Logic</h2>
        </div>
    </div>
</template>

<script>

export default {
    name: "SloganHolder"
}

</script>

<style scoped>

@media screen and (max-width: 750px) {
    #block-1-spacer, #block-2-spacer, #block-3-spacer, #block-4-spacer {
        width: 0px;
    }
    #slogan-main-container{
        height: 37vh;
        border-bottom: solid .25px grey;
    }
    img {
        height: 30px;
        width: 30px;
    }
}

@media screen and (min-width: 750px) {
    img{
        height: 60px;
        width: 60px;
    }
    #block-1-spacer{ 
        width: 15%; 
    }
    #block-2-spacer{
       width: 30%; 
    }
    #block-3-spacer{
       width: 45%; 
    }
    #block-4-spacer{
       width: 60%; 
    }
    #slogan-main-container{
        height: 96vh;
    }
}

#slogan-main-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 3%;
}

#slogan-main-container > div{
    display: flex;
    align-items: center;
    width: 100%;
    gap: 3%;
    margin:0;
    padding: 0;
}

img{
    margin: 0;
    padding: 0;
}

.slogan-icon {
    height: 50px;
    width: 50px;
}

.slogan-text {
    font-size: 26pt; 
    margin: 0;
    padding: 0;
    font-family: "Roboto Condensed", sans-serif;
    font-weight: 600;
    font-style: normal;
}

</style>
