<template>  

       
 
             <button @click="register()" class="searchbt">Register</button> 
               <button @click="login()" class="searchbt">Login</button> 
         

</template> 

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

<style>
.forme{
    padding-left:35px;
    width: 940px;
    padding-bottom: 30px;
    
}
.button{
    
    background-color: rgb(66, 66, 254);
    border-radius: 5px;
    padding:8px;
    text-align: center;
}

#model{
    padding-bottom:50px;
}
.b1{
   text-decoration: none;
   color: white;
   text-align: center;
   
}

#labelbt{
    padding-bottom:6px;
}
img{
    width: 350px;
    height:220px;
}

ul{
    list-style-type: none;
}

.cars__list{
    align-items: center;
    padding-top: 20px;
    display: grid;
    grid-template-columns: repeat(3,300px);
    grid-gap: 10px;
}

.tophead{
    display:flex;
    gap:20px;
}

.price{
    background-color: rgb(20, 160, 20);
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 5px;
    border-radius: 10px;
    color: white;
}

.searchbt{
    background-color: rgb(20, 160, 20);
    padding-left: 50px;
    padding-right: 50px;
    padding-bottom: 2px;
    border-radius: 5px;
    color: white;
}
.search{
    padding-top:30px;
    padding-bottom:30px;
    padding-left:80px;
    display: flex;
    gap:15px;
    border-radius: 5px;
    border: 1px solid rgb(96, 95, 95);
    background-color: white;
}

.searchitem{
    display: grid;
    grid-template-columns: repeat(1);
}
p{
    text-align: left;
}
#info{
    padding: 15px;
    text-align: left;
}
</style>
