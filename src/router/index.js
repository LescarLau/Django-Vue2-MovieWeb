import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Register from '../views/Register.vue'
import ActivateEmail from '../views/ActivateEmail.vue'
import Login from '../views/Login.vue'
import ResetPassword from '../views/ResetPassword.vue'
import PasswordReset from '../views/PasswordReset.vue'
import Personal from '../views/Personal.vue'
import ChangePassword from '../views/ChangePassword.vue'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/movie/:id',
    name:'MovieDetail',
    component:MovieDetail
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/register',
    name:'Register',
    component:Register
  },
  {
    path:'/login',
    name:'Login',
    component:Login
  },
  {
    path:'/reset_password',
    name:'ResetPassword',
    component:ResetPassword
  },
  {
    path:'/change_password',
    name:'ChangePassword',
    component:ChangePassword,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/personal',
    name:'Personal',
    component:Personal,
    meta:{
      requireLogin:true
    }
  },
  {
    path:'/activate/:uid/:token',
    name:'ActivateEmail',
    component:ActivateEmail
  },
  {
    path:'/password_reset/:uid/:token',
    name:'PasswordReset',
    component:PasswordReset
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

const token = localStorage.getItem('token')
if(token){
  store.commit('setLoginStatus',true)
}
//路由导航守卫
router.beforeEach((to,from,next)=>{
  if(store.state.isLogin && to.name==='Login' || to.name==='Register'){
    next({name:'home'})
  }else if(to.matched.some(record=>record.meta.requireLogin) && !store.state.isLogin){
    next({name:'Login',query:{jump:to.path}})
  }else{
    next()
  }
})

export default router
