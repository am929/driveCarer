<template>
<div class="bodyOfIt" style="height: 47rem;">
    <div class="container">
        <form action="">
          <h1>Login</h1>
          <div class="form">
              <div class="item">
                <label>用户名：</label><input type="text" name="username" v-model.trim="name" placeholder="请输入用户名">
                <!-- v-model把输入的值传输给name变量 -->
                <br/>
              </div>
              <div class="item">
                <label>密码：</label><input type="password" name="password" v-model.trim="password" placeholder="请输入密码">
                <br/>
              </div>
              <div class="keep">
                <input @click="handlesave" id="yes" type="radio" value="0" ><!-- 点击选中 -->
                <label for="yes">保持登录状态</label>
              </div>
          </div>
          
        </form>
              <button  type="submit" @click.prevent="handlelogin">登录            </button>
              <!-- v-on点击按钮触发handlelogin方法 -->
              <button  @click.prevent="handleregister">注册</button>
              <router-view></router-view>
    </div>
</div>
</template>
 
<style scoped>
.container{
  width: 100%;
  height: 35rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background:#f3f3ff;
  text-align: center;
  border-radius: 2rem;
  margin-top: -3rem;
}
.container h1{
  color: gray;
  margin-left: 2rem;
  margin-top: 4rem;
}
.item {
  color: gray;
  margin-left: 2rem;
  margin-top: 4rem;
  font-size: 2rem;
  text-align: left;
}
.item label{
  float:left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
input{
  margin-left: -0.5rem;
  padding: 1rem;
  border: solid 1px #4e5ef3;
  outline: 0;
  font: normal 1.5rem/100% Verdana,Tahoma,sans-serif;
  width: 50%;
  height: 20%;
  background:#f1f1f190;
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0.1rem;
}
button{
  position: relative;
  height: 3.5rem;
  width: 10rem;
  background: rgba(35, 19, 252, 0.425);
  border-radius: 1rem;
  margin-top: 2rem;
  box-shadow: none;
  color: white;
  margin-left: 4rem;
  margin-right: 1.5rem;
 
}
.keep{
  color: gray;
}
.keep input{
  width: 1.5rem;
  height: 1.5rem;
  margin-top: 1rem;
  margin-left: 1rem;
  margin-right: 0.5rem;
  margin-bottom: 1rem;
}
 
</style>
 
<script>
export default {
  data(){
    return{
      name:"",//姓名，用v-model绑定监听，将输入的字符串赋值给name变量
      password:"",//密码
      st:"false",//false为不保存登录
    };
  },
  methods:{
    handlelogin:function()
    {
      // 判断注册中的信息
      if(this.name===localStorage['name'] && this.password===localStorage['password'])
       {
         this.$router.replace('/home');//如果输入的名字以及密码正确路由跳转至个人页面
       } 
       else if(this.name==='')//名字为空
       {
         alert('用户名不为空');
       }
       else if(this.password==='')//密码为空
       {
         alert('密码不为空');
       }
      else{
         alert('账号不存在，请注册后登录');//查无此号
        }
    },
    handleregister:function()
    {
      this.$router.replace('/regester')//点击注册按钮，跳转至注册页面
    },
    //点击保持登录状态触发handlesave
    handlesave:function(){
      this.st="true";//修改登录状态为true
      localStorage.setItem('s',this.st);
      console.log(localStorage.s);
    }
  }
};
</script>