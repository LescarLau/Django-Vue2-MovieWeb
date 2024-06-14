<template>
  <div id="container" class="text-white text-sm bg-primary-300 min-h-screen pb-4"> 
    <Header/>
    <MovieList/>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
  components: {
    Header,Footer,MovieList
  }
}
</script>
