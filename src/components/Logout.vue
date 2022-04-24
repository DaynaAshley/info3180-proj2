<template>
    <h1>GoodBye</h1>
<form  id="logout" name="login" method="post" @submit.prevent="logout">
      
            <button class="button loginbtn">Login</button>
            
    </form>
</template>

<script>
     
export default {   
        data() {     
            return { 
            }  
            }, 
        created() {     
                this.logout();
            },
            
            methods: { 
                logout() {  
                    fetch("/api/auth/logout", {     
                        method: 'POST',
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
                }
            }
};
</script>


<style>

</style>
