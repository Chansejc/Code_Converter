<template>
    <div id="e-input-container">
        <input id="e-input" type="text" value="Email" 
            v-on:focus="clearEmailInput" 
            v-on:focusout="checkEmailAvailability" />
    </div>
    <div id="p-input-container">
        <input id="p-input" type="text" value="Password" 
            v-on:focus="clearPassInput"
            v-on:focusout="checkPassword"/>
    </div>
    <input id="input-submit-button" class="submit-button" type="submit" value="Login"
        v-on:click="handleSubmission" />
</template>

<script>
export default {
    name: "Inputs",
    methods: {
        getPassword() {
            let pHolder = document.getElementById("p-input");
            let password = "";

            if (pHolder.value != "" && pHolder.value != "Password") { password = pHolder.value; }
            else{ password = null; }
            return password;
        },
        getEmail() {
            let eHolder = document.getElementById("e-input");
            let email = "";

            if (eHolder.value != "" && eHolder.value != "Email") { email = eHolder.value; }
            else{ email = null; }
            return email;
        },
        clearPassInput() {
            let item = document.getElementById("p-input");
            item.value = "";
        },
        clearEmailInput() {
            let item = document.getElementById("e-input");
            item.value = ""
        },
        async handleSubmission() {
            console.log("Inside of handleSubmission");
            let result = await this.checkEmailAvailability();
            if(this.checkPassword()) {
                console.log(result);
                if(result){
                console.log("After checking password");
                let email = this.getEmail();
                let pw = this.getPassword();
                console.log("Trying to reach the endpoint");
                const Url = `http://127.0.0.1:5000/api/accounts/create/${email}/${pw}`;
                $.get(Url, function(d,s) {
                    console.log("in handleSubmission endpoint");
                    console.log(d.Status);
                    });
                }
            }
        },
        async checkEmailAvailability() {
            var curClass = document.getElementById('e-input-container').className.split(/\s+/)[0];
            if (curClass != "") $("#e-input-container").removeClass(curClass);
            let email = this.getEmail();
            const Url = `http://127.0.0.1:5000/api/accounts/email_available/${email}`;
            console.log("email >> ", email);
            if (email) {
                try{
                    const response = await fetch(Url);
                    if (!response.ok) throw new Error("Server response was not ok"); 
                    const result = await response.json();
                    console.log(result);
                    if (result.Status == "Fail"){ 
                        $("#e-input-container").addClass("input-unusable"); 
                        console.log("returning false");
                        return false; }
                    else { 
                        $("#e-input-container").addClass("input-usable") ;
                        console.log("returning true");
                        return true; };
                }catch (err){
                    console.log(err.message);
                } finally {
                    console.log("no longer loading");
                }

            } else {  
                console.log("returning false");
                $("#e-input-container").addClass("email-unusable"); 
                return false ;
            };
        },
        checkPassword() { //Needed Password Characteristics
            var curClass = document.getElementById('p-input-container').className.split(/\s+/)[0];
            $("#p-input-container").removeClass(curClass);
            let legal = true;
            const specialChars = "!@#$%^&*(){}[]|/";
            let pass = String(this.getPassword());
            console.log(pass);
            console.log(pass.length);
            let lenNeed, capsNeed, numNeed, scNeed = (8, 1, 2, 1);
            console.log("Checking password length");
            if (pass.length < lenNeed) { $("#p-input-container").addClass("input-unusable"); return false; }
            //let passList = pass.split('');
            let numCount = 0;
            let capsCount = 0;
            let scCount = 0;
            pass.split('').map((i) => {
                console.log("Checking if any invalid characters");
                if (i == "" || i == " " || i == '"' || i == "'") { $("#p-input-container").addClass("input-unusable"); return false; }
                else if (!(isNaN(i))) numCount++;
                else if (specialChars.includes(i)) scCount++;
                else if (i == i.toUpperCase) capsCount++;
            })
            console.log("Checking if all other factors pass");
            if ( numCount < numNeed || scCount < scNeed || capsCount < capsNeed ) legal = false;
            if (legal) $("#p-input-container").addClass("input-usable") ;
            else $("#p-input-container").addClass("input-unusable");
            console.log("returning legal", "Legal >>", legal);
            return legal
        },
    },
}
</script>

<style>
    
#e-input, #p-input{
    text-align: center;
    height: 60px;
    width: 250px;
    font-size: 14pt;
    border-radius: 25px;
    border: .25px grey;
    background-color: white;
    box-shadow: 1px 2px 4px 3px rgba(0,0,0,0.1);
}

#e-input-container, #p-input-container{
    width: 255px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 25px;
}

#input-submit-button{
    height: 65px;
    width: 100px;
    font-size: 14pt;
    border-radius: 2rem;
    border: none;
    box-shadow: 1px 2px 2px 3px rgba(0,0,0,0.1);
}

.input-unusable{
    box-shadow: 1px 2px 2px 3px rgba(227,81,61,2.1);
}

.input-usable{
    box-shadow: 1px 2px 2px 3px rgba(57,191,80,2.1);
}
</style>
