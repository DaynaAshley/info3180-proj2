<template>
  <H1>Add New Car</H1>
<div id="form_container">
  <form id="add_car" name="add_car" method="POST" enctype="multipart/form-data" @submit.prevent="addcar" >
    <div class="top">
          <div id="formgroup">
          <label> Make </label>
          <input type="text" name="make" id="make" required />
        </div>
        
         <div id="formgroup">
        <label> Model</label>
        <input type="text" name="model" id="model" required />
      </div>
    
     <div id="formgroup">
        <label>Colour</label>
        <input type="text" name="colour" id="colour" required />
    </div>
    
     <div id="formgroup">
        <label>Year</label>
        <input type="text" name="year" id="year" required />
    </div>
    
     <div id="formgroup">
        <label>Price</label>
        <input type="text" name="price" id="price" required />
    </div>
       
         <div id="formgroup">
          <label for="cartype">Car Type</label>
          <select name="cartype" id="cartype">
            <option value="SUV">SUV</option>
            <option value="Sedan">Sedan</option>
            <option value="Coupe">Coupe</option>
            <option value="HatchBack">HatchBack</option>
            <option value="Wagon">Wagon</option>
        </select>
        </div>

        <div id="formgroup">
      <label for="transmission">Transmission</label>
      <select name="transmission" id="transmission">
        <option value="Automatic">Automatic</option>
        <option value="Manual">Manual</option>
    </select>
    </div>
    
  </div>
   
    
    <div id="formgroup1">
    <label>Description</label>
    <textarea name="description" id="description" rows=5 cols=58 required  />
</div>

 <div id="formgroup1">
    <label>Upload Photo</label>
    <input type="file" name="photo" id="photo" required />
</div>
    <div class="btnpos">
      <button @click="explore()" class="send">Save</button>
    </div>
  </form>
  </div>
</template>

<script>
     
export default {   
        data() {     
            return {
                 csrf_token: '' 
            }  
            }, 
        created() {     
                this.getCsrfToken(); 
                localStorage.setItem('reloaded1', 'false');
                 localStorage.setItem('reloaded', 'false');
            },
            
            methods: { 
                explore(){
                   this.$router.push('/explore');
                  
               },
                addcar() {  
                    let addcarform = document.getElementById('add_car'); 
                    let form_data = new FormData(addcarform);
                    var myCookie = this.getCookie('token');
                    fetch("/api/cars", {     
                        method: 'POST', 
                        body: form_data,         
                        headers: { 

                           'Authorization': `Bearer ${myCookie}`,
                            'X-CSRFToken': this.csrf_token         
                            } 
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
            }
};
</script>


<style>
#form_container{
  padding-left:600px;
  width:1350px;
}

#add_car{
    background-color: white;
 border: 1px solid rgb(188, 188, 188);
    box-shadow: 0 2px 6px 3px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  padding: 30px;
  border-radius: 5px;
}
#formgroup,#formgroup1{
    display:grid;
    grid-template-columns: repeat(1);
}

#formgroup1{
  padding-bottom: 30px;
}

.top{
  display:grid;
  grid-template-columns: repeat(2,300px);
    grid-gap: 50px;
   padding-bottom: 40px;
}

h1 {
  padding-top: 20px;
  padding-bottom: 30px;
  padding-left: 600px;
}

.send {
  background: rgb(53, 193, 53);
  border: 0;
  padding-left:60px;
  padding-right: 60px;
  padding-top: 10px;
  padding-bottom: 10px;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  justify-content: center;
}

#formgroup input[type="text"]{
    padding: 10px;
    border-radius: 5px;
    border:1px solid rgb(188, 188, 188);
}

#photo{
    padding: 10px;
    border-radius: 5px;
    background-color: white;
}

select{
    width: 278px;
    background-color: white;
    padding: 10px;
    border-radius: 5px;
     border:1px solid rgb(188, 188, 188);

}

#description{
    border:1px solid rgb(188, 188, 188);
}

label{
    color: gray;
    font-weight: bold;
    padding-bottom: 5px;
}
</style>