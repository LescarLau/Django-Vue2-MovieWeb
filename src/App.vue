<template>
  <router-view/>
</template>

<script>
  export default{
    name:'App',
    beforeCreate(){
      this.$store.commit('initializeStore')
    },
  }
</script>