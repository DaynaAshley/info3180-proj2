<script>
     
export default {   
        data() {     
            return { 
            }  
            }, 
        created() {     
                this.logout();
                 this.$router.push('/');
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
