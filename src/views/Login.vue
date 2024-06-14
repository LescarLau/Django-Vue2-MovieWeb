<template>
    <div id="main-body" class="bg-primary-100 flex justify-center h-screen">
    <section class="container flex justify-center items-center rounded ">
        <div class="hidden md:block">
          <img src="../assets/images/bg.png" alt="" class="rounded-l max-h-[500px]">
        </div>
        <div class="rounded-r w-80 h-[500px] my-8 px-2 py-4 bg-white shadow shadow-gray-300">
          <div class="text-center text-lg py-6">用户登录</div>
          <form id="register_form" class="px-4">
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <input v-model="username" type="text"  placeholder="请输入用户名" class="outline-0 text-sm">
            </div>
            <div class="flex justify-left items-center relative h-10 px-4  my-2 rounded border-solid border border-gray-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-300 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
              <input v-model="password" type="password"  placeholder="请输入密码" class="outline-0 text-sm">
            </div>
            <div class="pt-6">
              <button v-on:click.prevent="submitForm" id="login" class="rounded bg-green-500 w-full h-8 text-white">登录</button>
            </div>
            <div class="text-center text-sm my-2"> 
              <span class="text-left text-green-500">
                <router-link to="/reset_password">忘记密码?</router-link>
              </span>              
              没有账号
              <a class="text-blue-500" href="/register">去注册</a>
            </div>
          </form>
        </div>
    </section>
</div>
</template>

<script>
import showMessage from '@/utils/message';
import axios from 'axios';
import { registerRuntimeCompiler } from 'vue';

export default{
    name:'Login',
    data:function(){
        return{
            username:'',
            password:''
        }
    },
    methods:{
        submitForm(){
            const username = this.username;
            const password = this.password;
            if(username===''){
                showMessage('用户名不能为空')
                return
            }
            if(password===''){
                showMessage('密码不能为空')
                return
            }
            const formData = {
                username:username,
                password:password,
            }
            axios.post('/api/jwt/create/',formData).then(response=>{
                const token = response.data.access;
                const refreshToken = response.data.refresh;
                const username = this.username;
                localStorage.setItem("token",token);
                localStorage.setItem("username",username);
                localStorage.setItem("refreshToken",refreshToken);
                localStorage.setItem("expiredTime",Date.now()+5*60*1000)
                const redirectAfterLogin = this.$route.query.jump
                const redirectUrl = redirectAfterLogin ? redirectAfterLogin : '/'
                console.log(redirectUrl)
                this.$store.commit('setLoginStatus',true)
                showMessage('登陆成功','info',()=>{
                    this.$router.push({
                        path:redirectUrl
                    })
                })
            }).catch(error=>{
                console.log(error)
                const errorData = error.response.data
                const errorMessages = Object.values(errorData).flat();
                for(let i = 0;i<errorMessages.length;i++){
                    showMessage(errorMessages[i])
                }
            })
        }
    }
}
</script>