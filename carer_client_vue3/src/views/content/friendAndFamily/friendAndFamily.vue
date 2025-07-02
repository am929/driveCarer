<script setup>
  import {ref} from 'vue'
  let title = ref('亲友界面')
  let lists = ref([
      {name:'大聪明', imageSrc:'../../../assets/image/大聪明.jpeg', relation:'妈妈', condition:'共享行程中'},
      {name:'小机灵', imageSrc:'../../../assets/image/小机灵.jpg', relation:'妻子', condition:'共享行程中'},
    ])
  //先是引入useRouter
  // import {useRouter} from 'vue-router'
  // export default {
  //   name:"liveView",
  //   setup(){
  //     const router = useRouter()
  //     //通过定义一个方法，使用router进行跳转
  //     const jump =()=>{
  //       router.push('/addFriendFamily')
  //     }
  //     return {
  //       //这里暴露一下jump方法
  //       jump
  //     }
  //   },
  // }
</script>

<template>
  <van-nav-bar
      style="background-color:#8888ff;height: 50px"
  >
    <template #title>
      <text class="title" style="font-size: 22px;color: white;padding-top: 20px;">好友列表</text>
    </template>

  </van-nav-bar>
  <div class="bodyOfIt">
<!--    <h1 class="title">{{title}}</h1>-->
    <div class="inside" v-for="v in lists" :key="v.imageSrc">
      <div class="insideLeft">
        <router-link to='/messageOfOthers'>
          <img class="image" src="../../../assets/image/小机灵.jpg" />
        </router-link>
      </div>
      <div class="insideRight" >
        <div><span class="top">{{v.name}}</span> </div>
        <div class="insideDiv"><span class="mid">{{v.relation}}</span> </div>
        <div><span class="bottom">{{v.condition}}</span> </div>
      </div>
      <div > <img src="../../../assets/image/错误.png" class="right" /></div>
    </div>
    <div class="button">
      <router-link to='/addFriendFamily'>
      <button  class="buttonBody" @click='jump'>
        添加亲友
      </button>
    </router-link>
    </div>
  </div>
</template>

<style scoped>
.inside{
  border: 1px #8888ff solid;
  border-radius: 2rem;
  height: 11rem;
  width: 95%;
  margin: 1rem auto;
}
.insideLeft{
  border: 1px solid #8888ff;
  border-radius: 1rem;
  height: 80%;
  width: 27%;
  margin: 1rem;
  margin-right: 0rem;
  display: inline-block;
  float: left;
}
.image{
  height: 100%;
  width: 100%;
  border-radius: 1rem;
}
.insideRight{
  /*border: 1px solid #8888ff;*/
  border-radius: 1rem;
  height: 85%;
  width: 55%;
  margin: 1rem;
  margin-right: 0rem;
  display: inline-block;
  float: left;
}
.top{
  color: #297fca;
  font-size: 2.2rem;
  margin-left: -10rem;

}
.insideDiv{
  margin: 0.8rem;
  margin-bottom: 1rem;
}
.mid{
  background-color: #f9c5e5;
  color: #7673e5;
  font-size: 1.3rem; 
  padding: 0.4rem;
  border-radius: 1rem;
  margin-top: 1rem;
  margin-left: -13rem;
}
.bottom{
  background-color: #b9f8bf;
  color: #2874e1;
  font-size: 1.3rem;
  margin-left: -9rem;
  padding: 0.4rem;
  border-radius: 1rem;
  margin-top: 1rem;
}
.right{
  /*border: 1px solid #8888ff;*/
  border-radius: 1rem;
  height: 20%;
  width: 7%;
  margin: 1rem;
  margin-left: 0rem;
  display: inline-block;
  float: left;
}
.button{
  border: 1px solid #8888ff;
  background-color: #8888ff;
  height: 8%;
  width: 80%;
  border-radius: 1rem;
  margin: 17rem auto;
  margin-top: 70%;
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
