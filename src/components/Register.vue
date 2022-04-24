<template>
    <h1>Register New User</h1>
    <div id="form_container">
    <form  id="register" name="register" method="POST" enctype="multipart/form-data" @submit.prevent="register" v-if="!savingSuccessful">
 <div class="top">
       <div id="formgroup">
    <label>Username</label>
    <input type="text" name="username" id="username" required/>
</div>

 <div id="formgroup">
    <label>Password</label>
    <input type="text" name="password" id="password" required/>
</div>

<div id="formgroup">
    <label>Fullname</label>
    <input type="text" name="fullname" id="name" required/>
</div>

 <div id="formgroup">
    <label>Email</label>
    <input type="email" name="email" id="email" required/>
</div>
 <div id="formgroup">
    <label>Location</label>
    <input type="text" name="location" id="location" required/>
</div>
</div>

 <div id="formgroup1">
    <label>Biography</label>
    <textarea name="biography" id="biography" rows=5 cols=58  maxlength="250" required/>
    </div>  

     <div id="formgroup1">
    <label>Upload Photo</label>
    <input type="file" name="photo" id="photo" required/>
    </div>
    <div class="btnpos">
         <button class="button send">Register</button>
    </div>
   
    </form>
</div>
</template>

<script>
     
export default {   
        data() {     
            return {
                 csrf_token: '',
                 text: "Successfully Registered!"
            }  
            }, 
        created() { 
              
                const reloaded = localStorage.getItem('reloaded');
                if (reloaded !== 'true') {
                    localStorage.setItem('reloaded', 'true');
                    location.reload();
                }    
                this.getCsrfToken(); 
            },
            
            methods: { 
               
                register() {  
                    let registerform = document.getElementById('register'); 
                    let form_data = new FormData(registerform);
                    fetch("/api/register", {     
                        method:'POST', 
                        body: form_data,         
                        headers: { 
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
                        this.$router.push({name:'login'})   
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
            }
};
</script>

<style>
#form_container{
  padding-left:600px;
  width:1350px;
}

#register{
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

#formgroup input[type="text"],#email  {
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

#biography{
    border:1px solid rgb(188, 188, 188);
}

label{
    color: gray;
    font-weight: bold;
    padding-bottom: 5px;
}
</style>