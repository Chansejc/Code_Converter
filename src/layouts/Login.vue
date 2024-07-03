<template>
    <div id="page-container"> 
        <div id="blank-side-container">
            <SloganHolder/>
        </div>
        <div id="login-form-container">
                <Title />
                <Inputs />
        </div>
    </div>
</template>

<script>
import SloganHolder from "../components/SloganHolder.vue";
import Title from "../components/Title.vue";
import Inputs from "../components/Inputs.vue";
export default {
    name: "Login",
    components: {
        SloganHolder,
        Title,
        Inputs
    },
    methods: {
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

@media screen and (min-width: 750px){
}

@media screen and (max-width: 750px) {
    #page-container {
        flex-direction: column;
        justify-content: space-evenly;
        align-items: center;
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

#blank-side-container{
    /*border: solid yellow 2px;*/
    width: 46vw;
}

</style>
