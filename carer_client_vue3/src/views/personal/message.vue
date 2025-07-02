<template>
  <!--  导航栏-->
  <van-nav-bar
      style="background-color:#8888ff;height: 50px"
      left-arrow
      @click-left="onClickLeft"
  >
    <template #title>
      <text style="font-size: 22px;color: white;">消息列表</text>
    </template>
  </van-nav-bar>
<!--下拉刷新,还没加上js代码-->
<!--  <van-pull-refresh v-model="loading" @refresh="onRefresh">-->
<!--    <p>刷新次数: {{ count }}</p>-->
<!--  </van-pull-refresh>-->

<!--消息-->
  <div style="background-color: #f9f9ff">
    <div style="padding-bottom: 100%;">
      <van-cell-group v-for="message in messages" >

        <van-cell  title="行程会话" size="large" to="#" style="padding: 30px" value="hah" >
          <template #icon>
            <van-icon v-if="message.messageType=='1'" name="chat-o" size="4rem" color="#96cf9c" style="padding-right: 15px"/>
            <van-icon v-if="message.messageType=='2'" name="bullhorn-o" size="4rem" color="#9bd7f9" style="padding-right: 15px"/>
          </template>
          <template #title >
            <span v-if="message.messageType=='1'" style="float:left;font-size: 20px;margin-left: 10px">行程消息</span>
            <span v-if="message.messageType=='2'" style="float:left;font-size: 20px;margin-left: 10px">系统提醒</span>

            <br/>
          </template>
          <template #label>
            <van-text-ellipsis style="float:left;margin-top:6px;font-size: 15px;margin-left: 10px" :content="message.messageContent" />
<!--            <span style="float:left;margin-top:6px;font-size: 20px;margin-left: 10px">{{ message.content }}</span>-->
          </template>
          <template #value>
            <span style="font-size: 20px">{{message.time}}</span>
          </template>
        </van-cell>

      </van-cell-group>

    </div>

  </div>
</template>

<script>
import { ref } from 'vue';
import { showToast } from 'vant';
import axios from "axios";


export default {

  data(){
    return{
      messages:[{
        messageType:1,
        messageContent:"Vant 是一个轻量、可定制的移动端组件库",
        time:"2023-4-1"
      },
        // {
        //   type:2,
        //   title:"系统提醒",
        //   content:"Vant 是一个轻量、可定制的移动端组件库",
        //   time:"2023-4-5"
        // },
        // {
        //   type:1,
        //   title:"系统提醒",
        //   content:"Vant 是一个轻量、可定制的移动端组件库",
        //   time:"2023-4-5"
        // },
      ]
    }
  },
  created() {
    axios.get('http://localhost:9001/personal/messagelist/'+this.$route.query.id).then((res)=> {
     //console.log(res)
      this.messages=res.data.data
      var _this=this;
      for(var i=0;i<_this.messages.length;i++){
        //原本时间格式，可以用这个判断显示字符串'2023-04-07T04:58:02.000+00:00'
        let index=_this.messages[i].time.indexOf('T')//改成'T'显示日期，改成'.'显示日期和时间
        //后期可以用当前时间判断显示日期还是显示时间，
        let index1=this.messages[i].time.indexOf('-')
        _this.messages[i].time=_this.messages[i].time.substring(index1+1,index)
    //    console.log(_this.messages[i])
      }

    })
/**  按时间排序，这一段没生效，不知道为啥，晚点再看看
    function compare(prop,align){
      return function(a,b){
        var value1=a[prop];
        var value2=b[prop];
        if(align=="positive"){//正序
          return new Date(value1)-new Date(value2);
        }else if(align=="inverted"){//倒序
          return new Date(value2)-new Date(value1);
        }
      }
    };
    var myDate=new Date;
    console.log(myDate)
    this.messages.sort(compare('time','inverted'));
**/
  },


methods(){




}
};
</script>

<style scoped>


</style>

