<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <div class="text-center text-2xl p-8">
            激活你的账号
        </div>
        <div class="flex items-center justify-center">
            <div class="w-1/4 p-4 bg-gray-100 rounded-lg shadow-lg">
                <div class="text-black text-center p-4">
                    请点击下方按钮，激活账号
                </div>
                <div class="flex justify-center">
                    <button v-on:click="activate" class="bg-green-500 text-white px-4 py-2 rounded">激活账号</button> 
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'
import showMessage from '@/utils/message.js'


export default {
    name: 'ActivateEmail',
    components: { Header, Footer},
    methods: {
        activate() {
            // 获取参数
            const uid = this.$route.params.uid 
            const token = this.$route.params.token
            const formData = {
                'uid': uid,
                'token': token
            }
            // 激活用户接口
            axios
              .post('/api/users/activation/', formData)
              .then(response => {
                  // 登录成功后回到登录页面
                  showMessage('账号激活成功，可以登录了','info',()=>{
                    this.$router.push({name: 'Login'});
                  })  
              })
              .catch( function(error) {
                // 遍历所有错误信息
                console.log(error)
                const errorData = error.response.data
                console.log(errorData)
                const errorMessages = Object.values(errorData).flat(); 
                for (let i = 0; i < errorMessages.length; i++) {
                  showMessage(errorMessages[i])
                }
              })
        }
    }
}
</script>