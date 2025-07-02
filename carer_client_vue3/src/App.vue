<template>
  <meta name="referrer" content="no-referrer">
<!--  <nav>-->
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link>-->
<!--  </nav>-->
  <van-tabbar route>
    <van-tabbar-item replace to="/friendAndFamily" icon="friends-o">亲友</van-tabbar-item>
    <van-tabbar-item replace to="/map" icon="home-o">首页</van-tabbar-item>
    <van-tabbar-item replace to="/PersonalIndex" icon="setting-o">我的</van-tabbar-item>
  </van-tabbar>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
