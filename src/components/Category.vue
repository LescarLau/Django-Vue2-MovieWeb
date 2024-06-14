<template>
    <ul class="hidden md:flex items-center space-x-4 ml-2">
        <li>
            <a href="/">首页</a>
        </li>
        <li>
            <a href="">热门</a>
        </li>
        <li v-for="cat in info.results" v-bind="cat.id" @click="toggle(cat)" class="dropdown-menu flex items-center relative hover: cursor-pointer select-none">
            {{ cat.category_name }}
            <span>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
            </span>

            <div :class="{hidden: !cat.hidden}"  class="dropdown-item-content absolute top-9 w-32 transition ease-in-out delay-150 z-50">
            <ul  class="bg-primary-700 py-2 px-4">
            <li class="plx-2 py-2">
                <a :href="'/?category_id='+cat.id">全部</a>
            </li>
            <li class="plx-2 py-2" v-for="region in regions" :key="region.id">
                <a :href="'/?category_id='+cat.id+'&region='+region.id">
                    {{ region.name }}
                </a>
            </li>
            </ul>
        </div>
        </li>
    </ul>
</template>

<script>
import axios from 'axios';

    export default{
        name:'Category',
        data:function(){
            return {
                info:'',
                regions:[
                    {id:1,name:'中国大陆'},
                    {id:2,name:'中国香港'},
                    {id:3,name:'中国台湾'},
                    {id:4,name:'欧美'},
                    {id:5,name:'日本'},
                    {id:6,name:'韩国'},
                    {id:7,name:'其他'},
                ]
            }
        },  
        methods:{
            get_category_info(){
                axios.get('/api/category').then(response=>{
                    this.info = response.data
                    console.log(this.info)
                })
            },
            toggle(category){
                category.hidden = !category.hidden
            }
        },
        mounted(){
            this.get_category_info()
        }
    }
</script>