<script setup>
  import {ref} from 'vue'
  let title = ref('亲友详细信息')
</script>

<template>
  <van-nav-bar
      style="background-color:#8888ff;height: 50px"
  >
    <template #title>
      <text class="title" style="font-size: 22px;color: white;padding-top: 20px;">亲友详细信息</text>
    </template>
  </van-nav-bar>
  <div class="bodyOfIt">
<!--    <h1 class="title">{{title}}</h1>-->
    <div class="imageDiv">
      <img class="image" src="../../../assets/image/小机灵.jpg" />
    </div>
    <div class="mesName" style="margin-top:1rem"><span class="mesText">姓名：</span></div>
    <div class="message" style="margin-top:2rem"><span class="reText">小机灵</span></div>
    <div class="mesName" style="margin-top:-2rem"><span class="mesText">关系：</span></div>
    <div class="message" style="margin-top: -2rem;"><span class="reText">妈妈</span></div>
    <div class="mesName" style="margin-left: -3rem;margin-top:-0.2rem; " ><span class="mesText" style="padding: 0rem;">电话号码：</span></div>
    <div class="message" style="margin-top: -2rem;"><span class="reText" style="font-size: 2rem; margin-left: -7rem;">13925132183</span></div>

    <div class="button">
      <router-link to='/editMessage'>
      <button  class="buttonBody" @click='jump'>
        拨打电话
      </button>
    </router-link>
  </div>
    <div class="button" style="margin-top:-24rem">
      <router-link to='/editMessage'>
      <button  class="buttonBody" @click='jump'>
        编辑信息
      </button>
    </router-link>
    </div>
  </div>
</template>

<style scoped>
.imageDiv{
  border: 1px solid #8888ff;
  border-radius: 1rem;
  height: 15%;
  width: 22%;
  margin: 3rem auto;
  margin-bottom: 0rem;
  
}
.image{
  height: 100%;
  width: 100%;
  border-radius: 1rem;
}
.mesName{
  /*border: 1px #8888ff solid;*/
  border-radius: 0.5rem;
  height: 5rem;
  width: 35%;
  margin: 4rem auto;
  margin-left: -1rem;
  margin-top: 0.5rem;
  display: inline-block;
  float: left;
}
.mesText{
  font-size: 2rem;
  position: absolute;
  display: inline;
  padding: 2rem;
  /*border: 1px black solid;*/
}
.reText{
  font-size: 2rem;
  position: absolute;
  margin-left: -5rem;
  margin-top: 0.5rem;
  display: inline;
  /*border: 1px black solid;*/
}
.message{
  border: 1px #8888ff solid;
  border-radius: 0.5rem;
  height: 5rem;
  width: 50%;
  margin: 4rem auto;
  margin-right: 4.5rem;
  margin-top: 1rem;
  display: inline-block;
  float: right;
}
.button{
  border: 1px solid #8888ff;
  background-color: #8888ff;
  height: 8%;
  width: 80%;
  border-radius: 1rem;
  margin: 25.5rem auto;
}
.buttonBody{
  background-color: #8888ff;
  height: 100%;
  width: 100%;
  border-radius: 1rem;
  margin: 0;
  color: white;
  font-size: 1.8rem;
}
</style>
