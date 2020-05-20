/*
 * @Author: BeanCB
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-19 20:47:40
 * @Description: file content
 * @FilePath: /Covo/frontend/src/main.js
 */ 
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'

Vue.use(ElementUI);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
