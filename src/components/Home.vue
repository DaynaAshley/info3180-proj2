<template>
    <div class="container">
      <div class="info">
        <h1>Buy and Sell Cars Online</h1>
        <p>United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online.
          Find a Great Price on the Vehicle You Want.
        </p>
        <div class="btnpos">
          <button @click="register()" class="button register">Register</button> 
          <button  @click="login()" class="button login">Login</button>
        </div>
      </div>
    
      <div class="photo">
           <img alt="stock pic" class="logo" src="@/assets/car.jpg"  />
       
      </div>

    </div> 
  
     
</template>

<style>
.container{
  display: flex;
  gap:350px;
}

.info{
    padding-top: 200px;

}

h1{
    font-weight: bolder;
    font-size: 60px;
    padding-bottom: 20px;
}
button{
    background: limegreen;
    border: 0;
    padding: 10px 20px; 
    padding-left: 40px;
    padding-right: 40px;
    color: white; 
    border-radius: 5px;
    justify-content: center;
}

.btnpos{
    display: flex;
    gap: 20px;
}

.logo{
    height:800px;
    width: 1000px;
}

.register{
    background:skyblue;
}


</style>

<script>
export default {   
        data() {     
            return {
            }  
            },   
            created(){
               const reloaded2 = localStorage.getItem('reloaded2');
                if (reloaded2 !== 'true') {
                    localStorage.setItem('reloaded2', 'true');
                    location.reload();
                   
                }
              
            } ,       
            methods: { 
               register() {         
                   this.$router.push('/register');   
                    },

                login() {
                    this.$router.push('/login'); 
              } 
            }
};
</script>

