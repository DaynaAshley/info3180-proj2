<template>
<link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
  <header>


    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/" id="main"><i id="home" class="fas fa-car"></i> United Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink id="loginto" class="nav-link" to="/register" v-if="user_id==''">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login" v-if="user_id==''">Login</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore" v-if="user_id!=''">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/cars/new" v-if="user_id!=''">Add Car</RouterLink>
            </li>
            
            <li class="nav-item" v-if="user_id!=''">
              
              <router-link :to="{ name: 'userdetails', params: { user_id } }" class="nav-link">My Profile</router-link>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" id="lg" to="/logout" v-if="user_id!=''">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>

import { RouterLink } from "vue-router";

export default {   
        data() {     
            return {
                user_id: ' '
            }  
        },    
        created(){
          let self=this;
            var myCookie =this.getCookie('user');
            self.user_id=myCookie;
        },        
            methods: { 
                getCookie(cname) {
                    let name = cname + "=";
                    let decodedCookie = decodeURIComponent(document.cookie);
                    let ca = decodedCookie.split(';');
                    for(let i = 0; i <ca.length; i++) {
                      let c = ca[i];
                      while (c.charAt(0) == ' ') {
                        c = c.substring(1);
                      }
                      if (c.indexOf(name) == 0) {
                        return c.substring(name.length, c.length);
                      }
                    }
                    return "";
              }
            }
};



</script>

<style>
#home{
  color: white;
}

#main{
  padding-left: 30px;
  padding-right: 220px;
}

#loginto{
  padding-left: 1200px;
}

#lg{
  padding-left: 1000px;
}
</style>