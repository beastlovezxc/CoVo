/*
 * @Author: FengSiJia
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-25 01:02:28
 * @Description: file content
 * @FilePath: /Covo/frontend/src/main.js
 */ 
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import axios from 'axios'
Vue.prototype.axios = axios
Vue.use(ElementUI);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
