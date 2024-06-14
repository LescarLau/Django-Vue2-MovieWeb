<template>
    <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
        <Header/>
        <div id="main" class="bg-primary-300 p-6 text-black">
            <div class="rounded bg-white mx-4 my-4 py-6 ">
                <div class="px-6">
                    <h1 class="text-lg font-semibold">个人中心</h1>
                </div>
            </div>
            <div class="rounded bg-white mx-4 mt-4 py-6 "> 
                <PersonalNav/>
                <div class="mt-4 mb-3 ">
                    <div class="not-prose relative">
                        <div class="ml-4 text-lg">
                        <div class="py-2 text-md">
                            <form  action="" method="post"  class="w-[300px]">
                            <div  class="flex items-center justify-between py-2">
                                <label for="old_password">原始密码:</label>
                                <input v-model="current_password" id="old_password" type="password" name="old_password" class="mx-2 outline-0 rounded border border-solid border-gray-500">
                            </div>
                            <div class="flex items-center justify-between py-2">
                                <label for="new_password">新密码:</label>
                                <input v-model="new_password" id="new_password" type="password" name="new_password" class="mx-2 outline-0 rounded border border-solid border-gray-500">
                            </div>
                            <div class="flex items-center justify-between py-2">
                                <label for="confirm">确认密码:</label>
                                <input v-model="re_password" id="confirm_password" type="password" name="confirm_password"  class="mx-2 outline-0 rounded border border-solid border-gray-500">
                            </div>
                            <button v-on:click.prevent="setPassword" type="button" id="change_password" class="mb-2 rounded border bg-blue-500 text-white text-sm h-8 w-16">提交</button>
                            </form>
                        </div>
                    </div>
                    </div>
                </div>          
            </div>
            </div>
        
        <Footer/>
    </div>
    </template>
    
    <script>
    import Header from '@/components/Header.vue'
    import Footer from '@/components/Footer.vue'
    import PersonalNav from '@/components/PersonalNav.vue'
    import axios from 'axios'
    import showMessage from '@/utils/message.js'
    import getAxiosResponseError from '@/utils/message.js'
    
    export default {
        name: 'ChangePassword',
        data: function(){
            return {
                current_password: '',
                new_password: '',
                re_password: '',
            }
        },
        components: {Header, Footer, PersonalNav},
        methods: {
            setPassword() {
               const current_password = this.current_password
               const new_password = this.new_password
               const re_password = this.re_password

               if (new_password !== re_password) {
                showMessage('2次密码不一致！')
                return 
               }
               const formData = {
                  current_password: this.current_password,
                  new_password: this.new_password,
                  re_new_password:this.re_password
               }
               const accessToken = window.localStorage.getItem('token'); 
               console.log(accessToken)
               axios 
                .post('/api/users/set_password/', formData, {
                    headers: {
                        'Authorization': `JWT ${accessToken}` 
                    }
                })
                .then( response => {
                    showMessage('修改成功,请重登录','info')
                    setTimeout(() => {
                        localStorage.clear();
                        window.location.reload(); 
                    }, 1000);
                } )
                .catch(error => {
                    // 遍历所有错误信息
                    const errorData = error.response.data
                    const errorMessages = Object.values(errorData).flat(); 
                    for (let i = 0; i < errorMessages.length; i++) {
                      showMessage(errorMessages[i])
                    }
                })
            }
        }
    }
    </script>