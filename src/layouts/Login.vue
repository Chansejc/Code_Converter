<template>
    <div class="page-container">
        <div class="login-form-container">
            
            <div class="u-input-container">
                <input id="u-input" type="text" value="Username"/>
            </div>

            <div class="p-input-container">
                <input id="p-input" type="text" value="Password"/>
            </div>

            <input id="input-submit-button" class="submit-button" type="submit" value="login"/>
        </div>
    </div>
</template>

<script>
export default {
   name: "Login" 
}
</script>

<style>
.login-form-container {
    border: solid 4px grey;
    height: 50%;
    width: 50%;
    display: flex;
    gap: 10%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

#u-input, #p-input{
    height: 100%;
    width: 100%;
    font-size: 18pt;
    text-align: center;
    border: none;
    color: grey ;
    border-radius: 2%;
    background: none;
}

.u-input-container, .p-input-container{
    height: 20%;
    width: 50%;
    border: solid #DDDDDD 2.5px; 
    border-radius: 5%;
}

.page-container{
    height: 98vh;
    width: 98vw;
    margin: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.submit-button{
    height: 10%;
    width: 15%;
    font-size: 18pt;
}
</style>
