<template> 

<ul class="user__list">
       
         <li v-for="user in users" class="users__item" v-bind:key="user in users">
            
                  <div class="infobody">  
                        <div class="top">  
                <img v-bind:src= "'/uploads/' + user.photo" class="user_img">   
                
                <h5 class="card-title">{{user.name}}</h5>   
                <p class="card-subtitle mb-2 text-muted">@{{user.username}}</p>  
                <p class="card-text">{{user.biography}}</p> 
                 </div> 
                <div id="info">
                  <p class="card-subtitle mb-2 text-muted">Email</p>
                    <p class="card-text">{{user.email}}</p>
                    <p class="card-subtitle mb-2 text-muted">Location</p>
                    <p class="card-text">{{user.location}}</p>  
                       <p class="card-subtitle mb-2 text-muted">Joined</p>
                    <p class="card-text">{{user.date_joined}}</p>
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
                <div class="tophead">    
                <h5 class="card-title">{{car.year}} {{car.make}}</h5>  
                <p class="price"><i class="fas fa-thin fa-tag" /> ${{car.price}}</p> 
                </div>  
                <p class="card-subtitle mb-2 text-muted" id="model">{{car.model}}</p> 
                <div class="button">
                 <router-link :to="'/cars/' + car.id" class="b1">View more details</router-link>
                 </div>    
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
.user_img{
    border-radius: 50%;
}

.infobody{
    display:flex;

}
.button{
    
    background-color: rgb(66, 66, 254);
    border-radius: 5px;
    padding:8px;
    text-align: center;
}

#model{
    padding-bottom:50px;
}
.b1{
   text-decoration: none;
   color: white;
   text-align: center;
   
}

#labelbt{
    padding-bottom:6px;
}
img{
    width: 350px;
    height:220px;
}

ul{
    list-style-type: none;
}

.cars__list{
    align-items: center;
    padding-top: 20px;
    display: grid;
    grid-template-columns: repeat(3,300px);
    grid-gap: 10px;
}

.tophead{
    display:flex;
    gap:20px;
}

.price{
    background-color: rgb(20, 160, 20);
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    border-radius: 10px;
    color: white;
}

.searchbt{
    background-color: rgb(20, 160, 20);
    padding-left: 50px;
    padding-right: 50px;
    padding-bottom: 2px;
    border-radius: 5px;
    color: white;
}
.search{
    padding-top:30px;
    padding-bottom:30px;
    padding-left:80px;
    display: flex;
    gap:15px;
    border-radius: 5px;
    border: 1px solid rgb(96, 95, 95);
    background-color: white;
}

.searchitem{
    display: grid;
    grid-template-columns: repeat(1);
}
p{
    text-align: left;
}
#info{
    display: grid;
    grid-template-columns: repeat(2);
    grid-gap: 10px;
}

</style>
