<template>  
  <!-- <form @submit.prevent="searchCar" class="d-flex flex-column justify-content-center">   
         <div class="input-group mx-sm-3 mb-2">         
             <label  for="make_search">Make </label>        
              <input type="search" name="make_search" v-model="searchMake" id="make_search" class="form-control mb-2 mr-sm-2" />     
              <label  for="model_search">Model</label>        
              <input type="search" name="model_search" v-model="searchModel" id="model_search" class="form-control mb-2 mr-sm-2" />            
              <button class="btn btn-primary mb-2">Search</button>       
         </div>        
    </form>  -->

     <ul class="cars__list"> 
         <li v-for="car in cars" class="cars__item" v-bind:key="car in cars">
              <img v-bind:src= car.photo />
              <div id="info">
                    <!-- <h5> {{ car.title }}</h5> -->
                    <p> {{ car.description}}</p>
               </div>
        </li>            
     </ul> 
</template> 

<script>
     
export default {   
        data() {     
            return {
                cars: [],
                csrf_token: '' 
            }  
            },            
            methods: { 
                
                getCsrfToken() {     
                    let self = this;     
                    fetch('/api/csrf-token')       
                    .then((response) => response.json())      
                     .then((data) => {         
                         console.log(data);         
                         self.csrf_token = data.csrf_token;   
                        })   
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
                    // let addcarform = document.getElementById('add_car'); 
                    // let form_data = new FormData(addcarform);
                    var myCookie = this.getCookie('token');
                    fetch("/api/cars", {     
                        method: 'GET',
                        // , 
                        // body: form_data,         
                        headers: { 

                           'Authorization': `Bearer ${myCookie}`
                        //    ,
                        //     'X-CSRFToken': this.csrf_token         
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

