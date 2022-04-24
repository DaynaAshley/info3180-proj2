<template>
    <a v-on:click="logout" href="#">Logout</a>
</template>

<script>

export default {

    name: 'Header', 
    methods: {

        logout()
        {

            document.cookie = "user" + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
            this.$router.push({name: 'home'})

        }
}

};

           
</script>

<style>
    

</style>
