<template>
    <div id="page-container"> 
        <div id="blank-side-container">
            <SloganHolder/>
        </div>
        <div id="login-form-container">
                <div id="top-title-container">
                    <h2 class="Caps title-letter">C</h2><p>o</p><p>d</p><p>e</p>
                </div>
                <div id="bottom-title-container">
                    <h2 class="Caps title-letter">C</h2><p>o</p><p>n</p><p>v</p><p>e</p><p>r</p><p>t</p><p>e</p><p>r</p>
                </div>
                <input id="u-input" type="text" value="Username"/>
                <input id="p-input" type="text" value="Password"/>
                <input id="input-submit-button" class="submit-button" type="submit" value="Login"/>
        </div>
    </div>
</template>

<script>
import SloganHolder from "../components/SloganHolder.vue";
export default {
    name: "Login",
    components: {
        SloganHolder
    }
}
</script>

<style>

#app{
    display: flex;
    justify-content: center;
    align-items: center;
}

#app > div{
    padding: 0;
    margin: 0;
}

#page-container{
    height: 96vh;
    width: 96vw;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    /*border: solid 2px green; */
    align-items: center;
}

@media screen and (max-width: 750px) {
    #page-container {
        flex-direction: column;
    }
    #login-form-container{
      box-shadow: none; 
      height: 35vh;
    }
    #blank-side-container{
        height: 35vh;
    }
}

@media screen and (min-width: 750px) {
    #login-form-container{
        box-shadow: -4px 0px 0px 0px rgba(0,0,0,.1);
        height: 94vh;
    }
    #blank-side-container{
        height: 94vh;
    }
}

#login-form-container {
    border: none;
    width: 48vw;
    display: flex;
    gap: 2rem;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

#u-input, #p-input{
    text-align: center;
    height: 60px;
    width: 250px;
    font-size: 14pt;
    border-radius: 25px;
    border: .25px grey;
    background-color: white;
    box-shadow: 1px 2px 4px 3px rgba(0,0,0,0.1);
}

.submit-button{
    height: 65px;
    width: 100px;
    font-size: 14pt;
    border-radius: 2rem;
    border: none;
    box-shadow: 1px 2px 2px 3px rgba(0,0,0,0.1);
}

#blank-side-container{
    /*border: solid yellow 2px;*/
    width: 46vw;
}

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
