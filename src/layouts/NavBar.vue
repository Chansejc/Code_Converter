<template>
    <div id="nav-container">
        <h1>Code Converter</h1> 
    </div>
</template>

<script>
export default {
    name: "NavBar",
    components:{},
}
</script>

<style>

#nav-container {
    border-bottom: solid rgba(0,0,0,.75) 1px;
    width: 98vw;
    height: 75px;
    background: white;
    display: flex;
    justify-content: start;
    align-items: center;
}

#nav-container > h1 {
    margin: 3vh 0 3vh 5vw;
    font-size: 32pt;
    font-weight: 600;
}

</style>
