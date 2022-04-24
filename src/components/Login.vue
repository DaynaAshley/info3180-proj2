<template>
    <h3>Login to your account</h3>
    <div id="form_container">
    <form  id="login" name="login" method="post" @submit.prevent="login">
        <div class="top">
            <div id="formgroup">
        <label>Username:</label>
        <input type="text" name="username" id="username" required/>
    </div>
            <div id="formgroup">

        <label>Password:</label>
        <input type="password" name="password" id="password" required/>
        </div>
        </div>
        <div class="btnpos">
            <button @click="explore()" class="loginbtn">Login</button>
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
            },
            
            methods: { 
               explore(){
                   this.$router.push('/explore');
                  
               },
                login() {  
                    let loginform = document.getElementById('login'); 
                    let form_data = new FormData(loginform);
                    fetch("/api/auth/login", {     
                        method: 'POST', 
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
                        this.$router.push({name:'explore'})
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
  padding-left:1000px;
  width:1400px;
}

#login{
    background-color: white;
  border: 1px solid rgb(188, 188, 188);
    box-shadow: 0 2px 6px 3px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  padding: 50px;
  padding-left: 60px;

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
  grid-template-columns: repeat(1,200px);
    grid-gap: 50px;
   padding-bottom: 40px;
}

h3 {
  padding-top: 20px;
  padding-bottom: 30px;
  padding-left: 1080px;
}

.loginbtn {
  background: rgb(53, 193, 53);
  border: 0;
  padding-left:110px;
  padding-right: 110px;
  padding-top: 10px;
  padding-bottom: 10px;
  color: white;
  font-weight: bold;
  border-radius: 5px;
  justify-content: center;
}

#formgroup input[type="text"],#password  {
    padding: 10px;
    border-radius: 5px;
    border:1px solid rgb(188, 188, 188);
}




label{
    color: gray;
    font-weight: bold;
    padding-bottom: 5px;
}
</style>