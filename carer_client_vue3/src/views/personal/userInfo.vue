<template>
  <meta name="referrer" content="no-referrer">
  <!--  导航栏-->
  <van-nav-bar
      style="background-color:#8888ff;height: 50px"
      left-arrow
      @click-left="onClickLeft"
  >
    <template #title>
      <text style="font-size: 22px;color: white;padding-top: 20px;">账号管理</text>
    </template>
  </van-nav-bar>
  <!--页面-->
  <div style="background-color: #f9f9ff">
    <!--  头像昵称-->

<!--    <text>{{testData.list.nickName}}</text>-->
    <!--  选项栏-->
    <div style="padding-top: 100px;padding-bottom: 150px;">
      <van-cell-group inset style="box-shadow: 1px 5px 0px 1px rgba(0, 0, 0, 0.2);">

        <van-cell title="头像"  title-class="imgClass" size="large"  center="true">
          <template #extra>
            <van-image
                width="80"
                height="80"
                radius="10"
                :src="user.Img"
                style="margin-right: 10px"
            />
          </template>
        </van-cell>
<!--        <van-uploader :after-read="afterRead" />-->

        <van-cell title="账号" style="padding: 8% 5%;" is-link :value="userid" value-class="valueChange" size="large" />
        <van-cell title="昵称" style="padding: 8% 5%;" is-link :value="user.nickname" value-class="valueChange" size="large" @click="showPopup"/>
        <van-popup v-model:show="show" round :style="{ padding: '64px' }" >
          <van-cell-group inset>
            <van-field
                v-model="value1"
                rows="2"
                autosize
                label="修改昵称"
                type="textarea"
                colon="true"
                :placeholder="user.nickname"
            />
          </van-cell-group>


        </van-popup>

        <van-cell title="电话" style="padding: 8% 5%;" is-link :value="user.phone" value-class="valueChange" size="large" />


      </van-cell-group>
<!--      <p>提示：{{this.$route.query.id}}</p>-->
    </div>

  </div>
</template>

<script>
import {reactive} from "vue";
import API from "@/plugins/axiosInstance";
import axios from "axios";
import { ref } from 'vue';

export default {
  name: "userInfo",
  data(){
    return{
      user:{
        Img:'https://gitee.com/yiliu6661/carer-img/raw/master/gou4.png',
        nickname:"user",
        phone:"1"
      },
      userid:this.$route.query.id,
    }
  },
  created() {
    const testData = reactive({
      list:[]
    });
    const _this=this;
    // API({
    //   url:'/personal/getinfo/'+this.$route.query.id,
    //   method:'get'
    // }).then((res)=>{
    //   //  alert('请求成功!');
    //   console.log(res)
    //   _this.user.nickname=res.data.data.nickName;
    //   _this.user.phone=res.data.data.phone;
    //   _this.user.Img=res.data.data.avatarImage;
    //
    // });
    axios.get('http://localhost:9001/personal/getinfo/'+this.$route.query.id).then(function (res) {
      console.log(res)
        _this.user.nickname=res.data.data.nickName;
        _this.user.phone=res.data.data.phone;
        _this.user.Img=res.data.data.avatarImage;
            })
 //   console.log(this.$route.query)
  },
  setup() {
    const onClickLeft = () => history.back();
    const show = ref(false);
    const showPopup = () => {
      show.value = true;
    };


    return {
      onClickLeft,
      show,
      showPopup,

    };
  },
  methods: {
    changeNickName(){
      // const _this=this;
      // let nickName='mirai'
      // let data1=JSON.stringify(nickName)
      // console.log(data1)
      // API({
      //   url:'/personal/editinfo/'+this.$route.query.id,
      //   dataType:'json',
      //   contentType:'application/json',
      //   method:'PUT',
      //   data:data1
      //
      //
      // }).then((res)=>{
      //   alert('请求成功!');
      //   console.log(res)
      // });
      let data1=[
        {
          nickName:"Mirai",
          phone:"17199925811"
        }
      ]
      console.log(data1[0])
      axios.put('http://localhost:9001/personal/editinfo/'+this.$route.query.id,data1[0]).then(function (resp) {
        // if(resp.data.code == 0){
        //   console
        //   let instance = Toast('添加成功');
        //   setTimeout(() => {
        //     instance.close();
        //     _this.$router.push('/addressList')
        //   }, 1000)
        // }
        console.log(resp)
      })


    }
  }
}
</script>

<style>
.valueChange{
  font-size: 20px;
  padding-right: 10px;
}
.imgClass{
  padding-right: 30%;
}
:root:root{
  --van-nav-bar-icon-color:white;
  --van-nav-bar-arrow-size:20px
}
</style>