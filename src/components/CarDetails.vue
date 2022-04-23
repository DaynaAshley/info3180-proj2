<template> 
<link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">


    <ul class="cars__list">
         <li v-for="car in cars" class="cars__item" v-bind:key="car in cars">
             <div class="info">
            <div class="card_img" >   
                <img v-bind:src= "'/uploads/' + car.photo" > 
            </div>  

            <div class="card_body">     
                <h1 class="card-title">{{car.year}} {{car.make}}</h1>   
                <h5 class="card-subtitle mb-2 text-muted">{{car.model}}</h5>  
                <p class="card-subtitle mb-2 text-muted">{{car.description}}</p> 
                <div id="info">
                    <div id="l">
                    <p class="card-subtitle mb-2 text-muted">Color</p>
                    <p class="card-text">{{car.colour}}</p>
                    </div>
                    <div id="l">
                    <p class="card-subtitle mb-2 text-muted">Body Type</p>
                    <p class="card-text">{{car.car_type}}</p> 
                    </div>
                    <div id="l">
                    <p class="card-subtitle mb-2 text-muted">Price</p> 
                    <p class="card-text">${{car.price}}</p>
                    </div>
                    <div id="l">
                    <p class="card-subtitle mb-2 text-muted">Transmission</p> 
                    <p class="card-text">{{car.transmission}}</p>
                    </div>
                </div>
                <div id="l2">
                <a href="#" class="btn btn-success">Email Owner</a>   
            

                <form @submit.prevent="addLike" id="addlike">   
            
                    <button id="like"><i id="heart" class="fas fa-heart" /></button>       
                
                </form> 
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
h1{
    padding-top: 25px;
}

h5{
    padding-bottom: 30px;
}
.info{
    display:flex;
    gap: 50px;
}
img{
    width: 500px;
    height:600px;
}

.cars__item{
    background-color: white;
    border: 1px solid black;
    border-radius: 5px;
    width:1100px
}

.cars__list{
    padding-top: 50px;
}
ul{
    list-style-type: none;
}

#info{
    padding-top: 20px;
    display:grid;
    grid-template-columns: repeat(2,150px);
    grid-gap:50px;
    padding-bottom: 100px;
}

#l{
    display:inline-flex;
    gap:10px
}

#l2{
    display: flex;
    gap:300px;
}

#heart{
   color: red;
}
#like{
    border-radius: 50%;
    background-color: white;

}
</style>
