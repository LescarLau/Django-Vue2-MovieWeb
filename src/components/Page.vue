<template>
    <div id="footer" class="flex items-center justify-center text-gray-500 pb-4" style="margin-bottom: 20px;">
      <!-- 上一页 -->
      <span class="page-link"   v-if="info.previous" @click="goToPage(prevPage)">
          <button class="w-8 h-8 rounded mx-1 my-1 text-gray-600 bg-gray-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
          </button>
      </span>
      <!-- 遍历每一页 -->   
      <div class="page-link"   v-for="page in pages" :key="page"  :class="{ active: page === current}">
          <button v-if="page === current" @click="goToPage(page)" class="w-8 h-8 rounded mx-1 my-1 bg-blue-500 text-white">{{ page }}</button>
          <button v-else-if="page === '...'"  class="w-8 h-8 rounded mx-1 my-1">{{ page }}</button>
          <button v-else @click="goToPage(page)" class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">{{ page }}</button>
      </div> 
      <!-- 下一页 -->
      <a class="page-link"   v-if="info.next" @click="goToPage(nextPage)">
          <button class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mx-auto" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
              </svg>
          </button>
      </a>
  </div>
  </template>
  
  <script>
    export default {
        props: ['info'],
    
        data() {
            return {
                current: 1
            }
        },
    
        computed: {
            lastPage() {
                let pageSize=12
                return Math.ceil(this.info.count/pageSize)
            },
            prevPage() {
                if (this.current > 1) {
                return this.current - 1
                }
                return 1
            },
            nextPage() {
                if (this.current < this.lastPage) {
                    console.log(this.current)
                return this.current + 1
                }
                return this.current
            },
        
            pages() {
                const pages = []
                
                for (let i = 1; i <= this.lastPage; i++) {
                if (i === 1 || i === this.lastPage || (i >= this.current - 1 && i <= this.current + 1)) {
                    pages.push(i)
                } else if (pages[pages.length - 1] !== '...') {
                    pages.push('...')
                }
                }
                
                return pages
            }
        },
    
        mounted() {
            this.current = this.getPageFromUrl()  
        },
    
        methods: {
            getPageFromUrl() {
                const page = Number(this.$route.query.page)
                return page ? page : 1
            },
        
            goToPage(page) {
                this.current = page
                // 获取当前参数
                const query = {...this.$route.query};
                console.log(query)
                // 更新page参数
                query.page = page;
                // 跳转并传参数对象
                this.$router.push({
                query
                })
            }
        }
    } 
  </script>
  