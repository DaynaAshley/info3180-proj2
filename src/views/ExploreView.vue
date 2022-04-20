<template>
    <div class="explore container">     
        <h2>Explore</h2>  
        <Explore /> 
     </div> 
</template> 


<script>
import Explore from '@/components/Explore.vue' 

export default {   
    data() {     
        return {};
        }, 
        components: { Explore }
    }; 
</script> 

<style>
h2{
    text-align: center;
    padding-bottom: 20px;
}
p{
    text-align: left;
}
</style> 