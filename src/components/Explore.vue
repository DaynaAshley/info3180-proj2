<template>  
<link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">
<div id="container">
        <div class="forme">
  <form @submit.prevent="searchCar"  >   
         <div class="search">         
             <div class="searchitem"> 
             <label  for="make_search">Make </label>        
              <input type="search" name="make_search" v-model="searchMake" id="make_search" class="form-control mb-2 mr-sm-2" />     
              </div>
                <div class="searchitem"> 
              <label  for="model_search">Model</label>        
              <input type="search" name="model_search" v-model="searchModel" id="model_search" class="form-control mb-2 mr-sm-2" />   
               
                </div>   
                 <div class="searchitem"> 
                      <label id="labelbt"> </label> 
             <button class="searchbt">Search</button> 
               
                </div> 
                         
         </div>   
               
    </form> 
</div>
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
    </div>
</template> 

<script>
     
export default {   
        data() {     
            return {
                cars: [],
                searchMake:'',
                searchModel:'',
                card_id:0,
            }  
            },            
            methods: { 
                
                searchCar() {         
                    let self = this;  
                    var myCookie = this.getCookie('token');       
                    fetch('/api/search?make='+ self.searchMake + '&model='+self.searchModel, 
                    {   
                        method: 'GET',
                        headers: {
                            'Authorization': `Bearer ${myCookie}`  }
                        })           
                        .then(function(response) {             
                            return response.json();           
                            })           
                            .then(function(data) {            
                                 console.log(data);            
                                  self.cars = data.cars;          
                            });      
                    },

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
                 localStorage.setItem('reloaded1', 'false');
                const reloaded = localStorage.getItem('reloaded');
                if (reloaded !== 'true') {
                    localStorage.setItem('reloaded', 'true');
                    location.reload();
                }
                    let self=this; 
                    var myCookie = this.getCookie('token');
                    fetch("/api/cars", {     
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
                }
             
};
</script>

<style>
.forme{
    padding-left:35px;
    width: 940px;
    padding-bottom: 30px;
    
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

.card{
    border: 1px solid rgb(188, 188, 188);
    box-shadow: 0 2px 6px 3px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
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
    border: 1px solid rgb(188, 188, 188);
    box-shadow: 0 2px 6px 3px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
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
    padding: 15px;
    text-align: left;
}
</style>
