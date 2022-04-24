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
        <!-- <img alt="Sample car" class="logo" src="@/assets/car.jpg" width=115%> -->
      </div>

    </div> 
  
     
</template>

<style>
.container{
  padding: none;
  display: grid;
  grid-template-columns: 1fr 2fr;
  text-align: center;
  margin: none;
  gap:none;
}
p{
  margin: 10px;
}
button{
    background: limegreen;
    border: 0;
    padding: 10px 20px; 
    margin-top: 20px; 
    color: white; 
    border-radius: 20px;
    justify-content: center;
    margin:4px;
}
.info {
  text-align: center;
}
.btnpos{
  text-align: center;
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
            methods: { 
               register() {         
                   this.$router.push('/');   
                    },

                login() {
                    this.$router.push('/login'); 
              } 
            }
};
</script>

