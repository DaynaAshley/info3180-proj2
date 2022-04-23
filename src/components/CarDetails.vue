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

              <form @submit.prevent="addLike" id="addlike">   
         
                <button id="like">Like</button>       
               
            </form> 
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
              },
              addLike() {         
                    let self = this;  
                    let likeform = document.getElementById('addlike'); 
                    let form_data = new FormData(likeform);
                    var myCookie = this.getCookie('token');   
                    var last_segment = window.location.pathname.split('/').pop();    
                    fetch(`/api/cars/${last_segment}/favourite`, 
                    {   
                        method: 'POST',
                        body: form_data,
                        headers: {
                            'Authorization': `Bearer ${myCookie}`,
                            'X-CSRFToken': this.csrf_token  }
                        })           
                         .then(function (response) {    
                        return response.json();     
                        })     
                        .then(function (data) {         
                            // display a success message         
                            console.log(data);    
                             })     
                            .catch(function (error) {         
                                console.log(error);     
                                });    
                    },
                getCsrfToken() {     
                    let self = this;     
                    fetch('/api/csrf-token')       
                    .then((response) => response.json())      
                     .then((data) => {         
                         console.log(data);         
                         self.csrf_token = data.csrf_token;   
                        })   
                } 
            },
             created() {  
                    let self=this;
                    this.getCsrfToken(); 
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
