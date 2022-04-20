<template>  
  <form @submit.prevent="searchCar" class="d-flex flex-column justify-content-center">   
         <div class="input-group mx-sm-3 mb-2">         
             <label  for="make_search">Make </label>        
              <input type="search" name="make_search" v-model="searchMake" id="make_search" class="form-control mb-2 mr-sm-2" />     
              <label  for="model_search">Model</label>        
              <input type="search" name="model_search" v-model="searchModel" id="model_search" class="form-control mb-2 mr-sm-2" />            
              <button class="btn btn-primary mb-2">Search</button>       
         </div>        
    </form> 

    <ul class="car__list"> 
    <li v-for="car in cars" class="car__item" v-bind:key="car in cars">
        <div class="card" style="width: 18rem;">   
            <img v-bind:src= car.photo class="card-img-top">   
            <div class="card-body">     
                <h5 class="card-title">{{car.year}} {{car.make}}</h5>  
                <p class="price">{{car.price}}</p>   
                <p class="card-subtitle mb-2 text-muted">{{car.model}}</p>     
                <a href="{{url_for('cars', card_id=car.id)}}" class="btn btn-primary">View more details</a>   
            </div> 
        </div>
      </li>            
    </ul> 
</template> 

<script> 
    export default {   
        data() {     
            return {
                 cars: [],
                 serarchMake:'',
                 searchModel:''
            }  
            }, 
            methods: { 
                searchCar() {         
                    let self = this;         
                    fetch('/api/search?make=&model='+ self.searchMake + self.searchModel+ '&language=en', 
                    {     
                        headers: {'Authorization': `Bearer ${request.cookies.get('token') }`}
                        })           
                        .then(function(response) {             
                            return response.json();           
                            })           
                            .then(function(data) {            
                                 console.log(data);            
                                  self.cars = data.cars;          
                            });      
                    }    
                 },
            viewall() {
                let self = this; 
                  fetch('/api/cars',
                 {
                     method: 'GET',
                    headers: {'Authorization': `Bearer ${request.cookies.get('token') }`}
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
img{
    width: 300px;
    height:200px;
}

ul{
    list-style-type: none;
}

/* .news__list{
    padding-top: 20px;
    display: grid;
    grid-template-columns: repeat(3,300px);
    grid-gap: 50px;
}

.news__list li{
    border: 1px solid var(--black);
    box-shadow: 0 2px 5px 3px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    width:300px;
    border-bottom: 10px solid green;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;  
} */

p{
    text-align: left;
}
#info{
    padding: 15px;
    text-align: left;
}
</style>
