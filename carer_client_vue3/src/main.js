import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vant from 'vant'
import 'vant/lib/index.css'
import axios from '@/plugins/axiosInstance.js'
import './mock/'
//import moment from 'moment'
import * as echarts from 'echarts'
import'./assets/font/iconfont.css'
import './config/rem'

createApp(App).use(Vant).use(echarts).use(store).use(router).mount('#app')
//const app = createApp(App);   //建立一个vue3app
//app.mount('#app');            //将这个vue3app全局挂载到#app元素上
//app.config.globalProperties.$axios=axios;  //配置axios的全局引用
//app.config.globalProperties.$moment = moment
//app.config.globalProperties.$echarts = echarts