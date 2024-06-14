import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin:false
  },
  getters: {
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('token')){
        state.isLogin = true
      }else{
        state.isLogin = false
      }
    },
    setLoginStatus(state,status){
      state.isLogin = status
    }
  },
  actions: {
  },
  modules: {
  }
})
