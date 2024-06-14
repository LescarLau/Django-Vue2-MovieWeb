<template>
<div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
    <Header/>
    <div class="text-center text-2xl p-8">
        重置密码
    </div>
    <div class="flex items-center justify-center">
        <div class="w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
            <div class="text-black text-center p-4">
                <p class=" font-bold py-4">请输入注册时的邮箱</p>
                <div>
                    <input v-model="email" class="outline-0 h-9 rounded border border-green-600">
                </div>
            </div>
            <div class="flex justify-center">
                <button v-on:click="resetPassword" class="bg-green-500 text-white px-4">发送</button>
            </div>
        </div>
    </div>
    <Footer/>
</div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import axios from 'axios';
import showMessage from '@/utils/message';
    export default{
        name:'ResetPassword',
        components:{
            Header,Footer
        },
        data:function(){
            return{
                email:''
            }
        },
        methods:{
            resetPassword(){
                const email = this.email.trim()
                axios.post('/api/users/reset_password/',{email:email}).then(response=>{
                    showMessage('邮箱已发送，请确认','info',()=>{
                        this.$router.push({
                            name:'Login'
                        })
                    })
                }).catch(error=>{
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