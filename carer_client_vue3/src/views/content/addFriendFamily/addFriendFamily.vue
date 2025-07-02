<script setup>
  import {ref} from 'vue'
  let title = ref('添加亲友')
  import permision from "./permission.js"
const kuCode = async () => {
    //扫描成功后跳转至已扫描列表
    // #ifdef APP-PLUS
    let status = await checkPermission();
    if (status !== 1) {
        return;
    }
    // #endif
    uni.scanCode({
      success: (res) => {
        console.log(res,"条码");
        if(res.result!=""){
        //扫描的条码
        }
      },
      fail: (err) => {
        // 需要注意的是小程序扫码不需要申请相机权限
      }
  });
}
// #ifdef APP-PLUS
  const  checkPermission= async(code)=> {
    let status = permision.isIOS ? await permision.requestIOS('camera') :
      await permision.requestAndroid('android.permission.CAMERA');
  
    if (status === null || status === 1) {
      status = 1;
    } else {
      uni.showModal({
        content: "需要相机权限",
        confirmText: "设置",
        success: function(res) {
          if (res.confirm) {
            permision.gotoAppSetting();
          }
        }
      })
    }
    return status;
  }
  // #endif

</script>

<template>

  <div class="bodyOfIt">
    <h1 class="title">{{title}}</h1>
    <div class="scanCode">
      <button class="scan-btn" type="primary" @click="kuCode">扫描二维码</button>
    </div>
    <div class="scanText">
      <span class="text" >请扫描二维码！</span>
    </div>

    <div class="back">
      <router-link to='/friendAndFamily'>
        <img src="../../../assets/image/返回5.png" class="imageBack" @click='jump'>
      </router-link>
    </div>
    <div class="alblum">
        <img src="../../../assets/image/相册.png" class="image">
    </div>
  </div>
</template>

<style scoped>
.scanCode{
  height: 50%;
  width: 80%;
  margin: 4.5rem auto;
  border: 1px #8888ff solid;
  border-radius: 2rem;
}
.scanText{
  height: 6%;
  width: 80%;
  margin: -3.5rem auto;
  /*border: 1px #8888ff solid;*/
  border-radius: 2rem;
}
.text{
  font-size: 2.5rem;
}
.back{
  height: 13%;
  width: 20%;
  margin: 5rem;
  border: 1px #8888ff solid;
  background-color: #f3f3ff;
  border-radius: 10rem;
  display: inline-block;
  float: left;
}
.alblum{
  height: 13%;
  width: 20%;
  margin: 5rem;
  border: 1px #8888ff solid;
  background-color: #f3f3ff;
  border-radius: 3rem;
  display: inline-block;
  float: right;
}
.image{
  width: 85%;
  height: 85%;
  padding-top: 0.5rem;
  
}
.imageBack{
  width: 85%;
  height: 85%;
  padding-top: 0.5rem;
  
}
</style>
