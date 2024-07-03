<template>
        <div id="top-title-container">
            <h2 class="Caps title-letter">C</h2><p>o</p><p>d</p><p>e</p>
        </div>
        <div id="bottom-title-container">
            <h2 class="Caps title-letter">C</h2><p>o</p><p>n</p><p>v</p><p>e</p><p>r</p><p>t</p><p>e</p><p>r</p>
        </div>
</template>

<script>
export default {
   name: "Title" 
}
</script>

<style>
#top-title-container, #bottom-title-container{
    display: flex;
    align-items: center;
}

#top-title-container > p, #bottom-title-container > p {
    font-family: "Roboto Condensed", sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 40pt;
    margin: 0;
    padding: 0;
}

#top-title-container > h2, #bottom-title-container > h2 {
    font-family: "Roboto Condensed", sans-serif;
    font-weight: 600;
    font-style: normal;
    font-size: 64pt;
    margin: 0;
    padding: 0;
}
</style>
