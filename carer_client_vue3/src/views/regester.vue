<template>
    <div class="bodyOfIt" style="height: 47rem;">
      <div id="contain">
        <h1>Register</h1>
 
        <div class="form">
          <label>用户名：</label><input type="text" v-model.trim="name"><br/>
        </div>
        <div class="form">
          <label>密码：</label><input type="password" v-model.trim="password"><br/>
        </div>
        <div class="form">
          <label>邮箱：</label><input type="email" v-model.trim="mail"><br/>
        </div>
        <div class="form">
          <label>手机号：</label><input type="tel" v-model.trim="tel"><br/>
        </div>
        <button @click.prevent="handlefinish">提交</button>
      </div>
    </div>
</template>
 
<style scoped>
#contain{
  width: 98%;
  height: 42rem;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background:#f3f3ff;
  text-align: center;
  border-radius: 2rem;
  margin-top: 0rem;
}
#contain h1{
  color: gray;
  margin-left: 2rem;
  margin-top: 4rem;
  margin-bottom: 3rem;
}
.form{
  color: gray;
  margin-left: 0rem;
  margin-top: 2rem;
  font-size: 2rem;
  text-align: left;
}
label{
  float:left;
  width: 5em;
  margin-right: 0.5em;
  margin-left: 1rem;
  text-align: right;
}
input,textarea{
  margin-left: 1rem;
  padding: 0.5rem;
  border: solid 1px #4e5ef3;
  outline: 0;
  font: normal 2rem/100% Verdana,Tahoma,sans-serif;
  width: 20rem;
  height: 2.2rem;
  background:#f1f1f190;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 0.4rem;
}
input:hover,textarea:hover,input:focus,textarea:focus{border-color:#0d0aa1;}
button{
  position: relative;
  height: 4.5rem;
  width: 18rem;
  background: rgba(35, 19, 252, 0.425);
  border-radius: 1rem;
  margin-top: 3rem;
  box-shadow: none;
  color: white;
  margin-left: 3rem;
}
</style>
 
<script>
export default {
    name:'regester',
    props: {
    msg: String
  },
  data(){
    return{
      name:"",
      password:"",
      mail:"",
      tel:""
  };
  },
  methods:{
  //点击完成按钮触发handlefinish
    handlefinish:function()
    {
      if(localStorage['name']===this.name)
      {
        alert("用户名已存在");//如果用户名已存在则无法注册
      }
      else if(this.name==='')
      {
        alert("用户名不能为空");
      }
      else{//将新用户信息存储到localStorage
        localStorage.setItem('name',this.name);
        localStorage.setItem('password',this.password);
        localStorage.setItem('mail',this.mail);
        localStorage.setItem('tel',this.tel);
        localStorage.setItem('s',"false");
        alert("注册成功");
        this.$router.replace('/login');//完成注册后跳转至登录页面
      }
    }
  }
};
</script>