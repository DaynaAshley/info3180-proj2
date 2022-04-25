import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('//index.html'),
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/login',
      name: 'login',
      
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',       
      name: 'logout',       
      component: () => import('../views/LogoutView.vue')
    },
    {
      path: '/register',       
      name: 'register',       
      component: () => import('../views/RegisterView.vue')
      
    },
    {
      path: '/explore',       
      name: 'explore',       
      component: () => import('../views/ExploreView.vue')
      
    },
    {
      path: '/cars/new',       
      name: 'carsnew',       
      component: () => import('../views/AddVehicleView.vue')
      
    },
    {
      path: '/cars/:card_id',
      name: "cardetails",
      component: () => import('../views/CarDetailsView.vue'),
    },
    ,
    {
      path: '/users/:user_id',
      name: "userdetails",
      component: () => import('../views/ProfileView.vue'),
    },
  ]
})

export default router
