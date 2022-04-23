<template>
    <div class="explore_container">     
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
    padding-left: 40px;
    padding-bottom: 20px;
}

.explore_container{
    padding-left: 350px;
}
</style> 