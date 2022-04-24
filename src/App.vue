<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader />


  <main>
    <RouterView />
  </main>
  
</template>

<style>
body {
  padding-top: 75px;
  background-color: rgb(241, 243, 243);
}


</style>