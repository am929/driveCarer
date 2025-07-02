import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PersonalIndex from '../views/personal/PersonalIndex.vue'
import userInfo from "@/views/personal/userInfo";
import message from "@/views/personal/message";
import driveInfo from "@/views/personal/driveInfo";


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/personalIndex',
    name: 'personalIndex',
    component: PersonalIndex
  },
  {
    path: '/personal/userInfo',
    name: '个人信息管理',
    component: userInfo
  },
  {
    path: '/personal/message',
    name: '消息',
    component: message
  },
  {
    path: '/driveInfo',
    name: '驾驶信息统计',
    component: driveInfo
  },
  {
    path: "/login",
    name: "login",
    component: () =>
        import("../views/login.vue")

  },
  {
    path: "/regester",
    name: "regester",
    component: () =>
        import("../views/regester.vue")
  },
  {
    path:'/home',
    name:'home',
    component:()=>import('../views/content/index.vue')
  },
  {
    path:'/friendAndFamily',
    name:'friendAndFamily',
    component:()=>import('../views/content/friendAndFamily/friendAndFamily.vue')
  },
  {
    path:'/addFriendFamily',
    name:'addFriendFamily',
    component:()=>import('../views/content/addFriendFamily/addFriendFamily.vue')
  },
  {
    path:'/editMessage',
    name:'editMessage',
    component:()=>import('../views/content/editMessage/editMessage.vue')
  },
  {
    path:'/messageOfOthers',
    name:'messageOfOthers',
    component:()=>import('../views/content/messageOfOthers/messageOfOthers.vue')
  },
  {
    path:'/map',
    name:'map',
    component:()=>import('../views/Index/map')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
