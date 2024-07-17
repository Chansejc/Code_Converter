<template>
        <div class="dropdown">
            <button :id="newID" class="dropbtn">{{this.title}}</button>
            <div class="dropdown-content">
                <a v-for="item in opts"  @click="this.title = item.name">{{ item.name }}</a>
            </div>
        </div>
</template>

<script>
let title = "Dropdown";
export default {
    name: "DropDown",
    props: ["opts", "newID"],
    data(){
        return{
            title
        }
    },
}
</script>

<style>

.dropbtn {
    height: 80%;
    weight: 80%;
    border: solid black 1px;
    background: white;
    color: grey;
    border: none;
    font-size: 12pt;
    text-align: start;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    display:flex;
    justify-content: center;
    align-items: center;
    background-color: white;
    box-shadow: 0px 1px 1px 0px rgba(0,0,0,0.2);
    font-size: 14pt;
    font-weight: 400;
    text-align: center;
    width: 165px;
    height: 40px;
    border-radius: 10px;
    color: #DDDDDD;
    border: solid 0.4px;

}
/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 4px 8px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 8px 12px;
  text-decoration: none;
  display: inline-block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: inline-block;}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: #3e8e41;}
</style>
