<template>
  <meta name="referrer" content="no-referrer">
<!--  导航栏-->
  <van-nav-bar
      right-text="管理"
      style="background-color:#8888ff;height: 50px"
  >
    <template #title>
      <text style="font-size: 22px;color: white;padding-top: 20px;">个人信息</text>
    </template>
    <template #right>
      <text style="font-size: 20px;padding-top: 3px;color: white">管理</text>
    </template>
  </van-nav-bar>
<!--页面-->
<div style="background-color: #f9f9ff">
<!--  头像昵称-->
  <div style="padding-top: 70px;">
  <van-row>
    <van-col span="4" offset="3">
      <van-image
        width="100"
        height="100"
        radius="5"
        :src="data1.list.avatarImage"
    /></van-col>
    <van-col span="6" offset="6" style="padding-top: 20px">
      <van-cell-group inset="true" border="true" style="padding:10px;">
        <text style="font-size: 20px;">{{data1.list.nickName}}</text>
      </van-cell-group>

    </van-col>
  </van-row>
  </div>
<!--<text>{{testData.list}}</text>-->
<!--  选项栏-->
  <div style="margin-top: 90px;padding-bottom: 150px;">
    <van-cell-group inset style="box-shadow: 1px 5px 0px 1px rgba(0, 0, 0, 0.2);">
      <van-cell title="账号管理"  is-link size="large" @click="toInfo" />
      <van-cell title="驾驶信息统计" is-link size="large" @click="toDriveInfo"/>
      <van-cell title="消息" is-link size="large" @click="toMessage"/>
      <van-cell title="设置" is-link size="large" to="#"/>
      <van-cell title="意见反馈" is-link size="large"  to="#"/>

    </van-cell-group>

  </div>

<!--  <van-cell-group>-->
<!--    <van-cell title="单元格" value="内容" />-->
<!--    <van-cell title="单元格" value="内容" label="描述信息" />-->
<!--  </van-cell-group>-->
<!--  <van-cell-group inset>-->
<!--    <van-cell title="单元格" value="内容" />-->
<!--    <van-cell title="单元格" value="内容" label="描述信息" />-->
<!--  </van-cell-group>-->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { reactive } from 'vue'
import API from "../plugins/axiosInstance.js"


export default {

  name: 'HomeView',

  components: {
    HelloWorld
  },
  data(){
    return {
      data:{
       nickname:"xixi",
        imgurl:'https://gitee.com/yiliu6661/carer-img/raw/master/gou4.png'
      },
      list:[]
    };
  },
  setup(){
    //数据
    const data1 = reactive({
      list:[]
    });
    const _this=this;
    //测试请求方法

      API({
        url:'/personal/getinfo/528482306',
        method:'get'
      }).then((res)=>{
      //  alert('请求成功!');
        console.log(res)
        data1.list = res.data.data;
  //       _this.data.nickname=res.data.data.nickName;

      });
    return{
      data1,

    }
  },
  methods:{
   toInfo:function(){
     // const that=this
      setTimeout(()=>{
        this.$store.state.id=this.data1.list.id
        //console.log(this.$store.state.id)
        this.$router.push({path:'personal/userInfo?userId=',query:{id:this.data1.list.id}})
      },1000)
    },
    toMessage:function(){
      // const that=this
      setTimeout(()=>{
        this.$store.state.id=this.data1.list.id
        //console.log(this.$store.state.id)
        this.$router.push({path:'personal/message?userId=',query:{id:this.data1.list.id}})
      },1000)
    },
    toDriveInfo:function(){
      // const that=this
      setTimeout(()=>{
        this.$store.state.id=this.data1.list.id
        //console.log(this.$store.state.id)
        this.$router.push({path:'personal/driveInfo?userId=',query:{id:this.data1.list.id}})
      },1000)
    }
  }
}
</script>
<style>
:root:root {
  /*--van-cell-icon-size: 50px;*/
  --van-cell-group-title-line-height:54px;
  --van-cell-line-height:35px;
  --van-cell-large-title-font-size:20px
}
</style>