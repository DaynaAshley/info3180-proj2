<template> 
<ul class="cars__list">
       
         <li v-for="car in cars" class="cars__item" v-bind:key="car in cars">
              <div class="card" style="width: 18rem;">   
            <img v-bind:src= "'/uploads/' + car.photo" class="card-img-side">   
            <div class="card-body">     
                <h5 class="card-title">{{car.year}} {{car.make}}</h5>   
                <p class="card-subtitle mb-2 text-muted">{{car.model}}</p>  
                <p class="card-text">{{car.description}}</p> 
                <p class="card-text">{{car.model}}</p>
                <div id="info">
                    <p class="card-text">Color {{car.colour}}</p>
                    <p class="card-text">Body Type{{car.car_type}}</p>  
                    <p class="card-text">Price {{car.price}}</p>
                    <p class="card-text">Transmission {{car.transmission}}</p>
                </div>
                <a href="#" class="btn btn-primary">Email Owner</a>   
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
                    fetch(`/api/cars/${last_segment}`, {     
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
