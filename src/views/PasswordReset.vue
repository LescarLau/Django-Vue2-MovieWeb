<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
    <Header/>
    <div class="flex justify-center text-2xl p-8">
        重置密码
    </div>
<div class=" flex justify-center">
    <div class=" w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
        <div class=" text-black py-4">
            <div class=" items-start py-4 flex justify-center">
                <span>新密码:</span>
                <input v-model="new_password" id="new_password" type="password" name="new_password" class="mx-2 outline-0 rounded border border-solid border-green-500">
            </div>
            
            <div class="items-start py-4 flex justify-center">
                <span>确认密码:</span>
                <input v-model="re_new_password" id="confirm_password" type="password" name="confirm_password"  class="mx-2 outline-0 rounded border border-solid border-green-500">
            </div>
            <div class=" flex justify-center">
                <button v-on:click="passwordReset" type="button" id="change_password" class="mb-2 rounded border bg-green-500 text-white text-sm h-8 w-16">提交</button>
            </div>
        </div>
    </div>
</div>              
<Footer/>
</div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import showMessage from '@/utils/message';
import axios from 'axios';
    export default{
        name:'PasswordReset',
        components:{
            Header,Footer
        },
        data:function(){
            return{
                new_password:'',
                re_new_password:'',
            }
        },
        methods:{
            passwordReset(){
                const uid = this.$route.params.uid
                const token = this.$route.params.token
                const new_password = this.new_password.trim()
                const re_new_password = this.re_new_password.trim()
                if(new_password!==re_new_password){
                    showMessage('两次密码输入不一致','error')
                    return
                }
                const formData={
                    uid:uid,
                    token:token,
                    new_password:new_password,
                    re_new_password:re_new_password,
                }
                axios.post('/api/users/reset_password_confirm/',formData).then(
                    response=>{
                        showMessage('密码重置成功','info',()=>{
                            this.$router.push({
                                name:'Login'
                            })
                        })
                    }
                ).catch(error=>{
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