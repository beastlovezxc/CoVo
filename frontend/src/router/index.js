/*
 * @Author: BeanCB
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-21 22:45:31
 * @Description: file content
 * @FilePath: /Covo/frontend/src/router/index.js
 */ 
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('../views/Main.vue')
  },
  {
    path: '/info',
    name: 'info',
    component: () => import('../components/Information.vue')
  },
  {
    path: '/regist',
    name: 'regist',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/regist.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
