<script setup>
  import {ref} from 'vue'
  let lists = ref([
      {title:'亲友', icon:'icon-pengyou', path:'/friendAndFamily'},
      {title:'首页', icon:'icon-shouye', path:'/home'},
      {title:'我的', icon:'icon-wode', path:'/home'}

    ])
</script>

<template>
  <div class="bottom">
    <div class="footer"> </div>
    <div class="footer-seat">
      <div class="footer-lists">
        <ul>
          <li v-for="v in lists" :key="v.path">
            <router-link :to="v.path" activate-class="selected">
              <i class="iconfont" :class="v.icon" style="color: gray; fontSize:2.2rem"></i>
              <span style="color:gray;">{{v.title}}</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bottom{
  bottom: 0rem;
  background-color: #f3f3ff;
  color: gray;
}
ul{
  list-style-type: none;
  background-color: #f3f3ff;
  padding: 0;
  margin: 0;
  color: gray;
}
li{
  background-color: #f3f3ff;
  float: left;
  /*margin-left: 2rem;*/
  padding: 1rem 3.58rem;
 /* padding-left: 3.5rem;
  padding-right:3.5rem;*/
  font-size: 1.5rem;
  /*border: 1px gray solid;*/
  
}
.selected{
  color: #3fa2f7;
}

</style>
