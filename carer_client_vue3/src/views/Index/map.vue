<template>
  <van-nav-bar

      style="background-color:#8888ff;height: 50px"
  >
    <template #title>
      <text style="font-size: 22px;color: white;padding-top: 20px;">导航</text>
    </template>
  </van-nav-bar>
  <div class="app-container">
    <div style="background-color: #ffffff;">
      <div id="container"></div>
    </div>
  </div>

  <div >
    <van-cell-group inset style="padding: 20px ">
      <div>
        <span style="float: left;font-size: 15px">眨眼：</span>
        <span style="width: 80%;float: right;margin-top: 5px">
        <van-progress :percentage="75" stroke-width="12"  pivot-text=""/></span>
      </div>
      <div style="margin-top: 30px">
        <span style="float: left;font-size: 15px">哈欠：</span>
        <span style="width: 80%;float: right;margin-top: 5px">
        <van-progress :percentage="2" stroke-width="12" pivot-text=""/></span>
      </div>

      <div style="margin-top: 60px">
        <span style="float: left;font-size: 15px">转头：</span>
        <span style="width: 80%;float: right;margin-top: 5px">
        <van-progress :percentage="33" stroke-width="12" pivot-text=""/></span>
      </div>


    </van-cell-group>
  </div>
</template>

<script setup>
import AMapLoader from '@amap/amap-jsapi-loader';
/*在Vue3中使用时,需要引入Vue3中的shallowRef方法(使用shallowRef进行非深度监听,
因为在Vue3中所使用的Proxy拦截操作会改变JSAPI原生对象,所以此处需要区别Vue2使用方式对地图对象进行非深度监听,
否则会出现问题,建议JSAPI相关对象采用非响应式的普通对象来存储)*/
import { shallowRef } from '@vue/reactivity';
import {ref} from "vue";

// const map = shallowRef(null);
const path = ref([]);
const current_position = ref([]);

function initMap() {
  window._AMapSecurityConfig = {
    securityJsCode: 'a50910c4562c4650ae846dcc11be8e5a',
  }
  AMapLoader.load({
    key:"61f6ecaf03bdd99bdc32c90557286c7e", // 申请好的Web端开发者Key，首次调用 load 时必填
    version:"2.0", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    plugins:[''], // 需要使用的的插件列表，如比例尺'AMap.Scale'等
  }).then((AMap)=>{
    const map = new AMap.Map("container",{  //设置地图容器id
      viewMode:"3D",    //是否为3D地图模式
      zoom:13,           //初始化地图级别
      center:[113.041381,23.078265], //初始化地图中心点位置
    });




  }).catch(e=>{
    console.log(e);
  })
}
 initMap()
</script>


<style>
#container{
  padding:0px;
  margin: 0px;
  width: 100%;
  height: 450px;
}
</style>
