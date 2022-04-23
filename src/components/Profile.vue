<template> 

<ul class="user__list">
       
         <li v-for="user in users" class="cars__item" v-bind:key="user in userss">
              <div class="card" style="width: 18rem;">   
            <img v-bind:src= "'/uploads/' + user.photo" class="card-img-side">   
            <div class="card-body">     
                <h5 class="card-title">{{user.name}}</h5>   
                <p class="card-subtitle mb-2 text-muted">@{{user.username}}</p>  
                <p class="card-text">{{user.biography}}</p> 
                <div id="info">
                    <p class="card-text">Email {{user.email}}</p>
                    <p class="card-text">Location {{user.location}}</p>  
                    <p class="card-text">Joined {{user.date_joined}}</p>
                </div>
            </div> 
        </div>
</li>
</ul> 


<h3>Car Favourited</h3>
 <ul class="cars__list"> 
    <li v-for="car in cars" class="cars__item" v-bind:key="car in cars">
        <div class="card" style="width: 18rem;">   
            <img v-bind:src= "'/uploads/' + car.photo" class="card-img-top">   
            <div class="card-body">     
                <h5 class="card-title">{{car.year}} {{car.make}}</h5>  
                <p class="price">{{car.price}}</p>   
                <p class="card-subtitle mb-2 text-muted">{{car.model}}</p>     
                 <router-link :to="'/cars/' + car.id" >View more Details</router-link>
            </div> 
        </div>
      </li>            
    </ul> 

</template> 

<script>
     
export default {   
        data() {     
            return {
                users: [],
                cars: [],
                
            }  
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
            },
             created() {  
                    let self=this;
                    var myCookie = this.getCookie('token');
                    var last_segment = window.location.pathname.split('/').pop();
                    fetch(`/api/users/${last_segment}/favourites`, {     
                        method: 'GET',       
                        headers: { 
                           'Authorization': `Bearer ${myCookie}`      
                            } 
                        })     
                        .then(function(response) {
                        return response.json();
                        })
                        .then(function(data) {
                        console.log(data);
                        self.cars = data.cars;
                        });
                    fetch(`/api/users/${last_segment}`, {     
                        method: 'GET',       
                        headers: { 
                           'Authorization': `Bearer ${myCookie}`      
                            } 
                        })     
                        .then(function(response) {
                        return response.json();
                        })
                        .then(function(data) {
                        console.log(data);
                        self.users = data.users;
                        });
                }
};
</script>

<style>

</style>
