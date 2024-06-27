<template>
    <div class="login-container">
        <div class="login-leftside">
        </div>
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
    background-color: #686D76;
}

#u-input, #p-input{
    height: 100%;
    width: 100%;
    font-size: 18pt;
    text-align: center;
    border-radius: 25px;
    border: none;
    background-color: white;
    box-shadow: 0px 0px 0px 3px rgba(0,0,0,0.1);
}

.u-input-container, .p-input-container{
    height: 20%;
    width: 50%;
    border: none;
    background: none;
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
    font-size: 6pt;
}
</style>
