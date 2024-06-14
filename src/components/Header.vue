<template>
    <div id="header" class="h-12 py-1 bg-primary-100 flex items-center justify-center">
    <div class="w-full px-4" style="max-width:1440px;">
      <div class="flex justify-between" >
        <div class="flex items-center">
          <a href="/">
            <img  src="../assets/images/logo.png" style="height:39px" >
          </a>
          <div id="nav" class="px-4">
            <category/>
          </div>
        </div>
        <!-- 输入框 -->
        <div class="flex items-center space-x-2">
          <div class="relative shrink" >
            <form >
              <input v-model="keyword"  type="text" name="keyword"  class="
                      outline-0
                      h-9
                      rounded
                      bg-primary-700
                      border
                      border-gray-600
                      placeholder-gray-400
                      w-64
                      px-2
                      py-1
                      max-w-[180px]
                  "  placeholder="请输入关键词" >
              <div class="
                      absolute
                      top-0
                      right-0
                      flex
                      items-center
                      h-full
                  ">
                  <div class=" rounded text-xs text-gray-400 px-2 mr-2">
                      <button v-on:click.prevent="searchMovies">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                      </button>
                  </div>
              </div>
            </form>
          </div>
          <div v-if="$store.state.isLogin" id="userinfo" class="flex relative hover: cursor-pointer items-center justify-center rounded border border-solid text-white text-lg h-9 text-center">
                <div id="username" class="px-2">{{ username }}</div>
                <div  @click="toggleMenu" class="pr-2">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </div>
                
                <div :class="{hidden: !showMenu}" id="userinfo_menu" class="absolute top-[40px] w-32 transition ease-in-out delay-150 z-50">
                  <ul class="bg-primary-700 py-2 px-4 text-sm">
                    <li class="plx-2 py-2">
                      <a href="/personal">个人中心</a>
                    </li>
                    <li class="plx-2 py-2">
                      <a href="/collect">我的收藏</a>
                    </li>
                    <li class="plx-2 py-2">
                      <router-link to="/" v-on:click.prevent="logout()">退出</router-link>
                    </li>
                  </ul>
                </div>
              </div>
          <div v-else class="text-white flex-shrink-0 pr-2">
              <a href="/login/">登录</a> /
              <a href="/register/">注册</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>

<script>
import Category from '@/components/Category.vue';
import axios from 'axios';

export default {
  name: 'Header',
  data:function(){
    return{
      keyword:'',
      showMenu:false,
      username:''
    }
  },
  mounted(){
    this.username = localStorage.getItem('username')
    //判断登录状态
    const currentTime = Date.now()
    const expiredTime = localStorage.getItem('expiredTime')
    const refreshToken = localStorage.getItem('refreshToken')
    if(expiredTime>currentTime){
      this.$store.commit('setLoginStatus',true)
    }else if(refreshToken){
      axios.post('/api/jwt/refresh/',{refresh:refreshToken}).then(response=>{
        const token = response.data.accesss
        localStorage.setItem("token",token)
        //更新过期时间
        const expiredTime = Date.now() + 5*60*1000
        localStorage.setItem('expiredTime',expiredTime)
      }).catch(error=>{
        this.$store.commit('setLoginStatus',false)
        localStorage.clear()
      })
    }else{
      this.$store.commit('setLoginStatus',false)
      localStorage.clear()
    }
  },
  components:{
    Category
  },  
  methods:{
    searchMovies(){
      const keyword = this.keyword.trim() //去除前后空格
      this.$router.push({
        name:'home',
        query:{search:keyword}
      })
    },
    toggleMenu(){
      this.showMenu = !this.showMenu
    },
    logout(){
      localStorage.clear()  //清空本地数据
      this.$store.commit('setLoginStatus',false)
    }
  }
}
</script>