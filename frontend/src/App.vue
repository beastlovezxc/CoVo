<!--
 * @Author: BeanCB
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-18 23:13:24
 * @Description: file content
 * @FilePath: /Covo/frontend/src/App.vue
 -->
<template>
  <div id="app">
    <div id="nav">
      <div id="head">
        <router-link to="/">登录</router-link>  |
        <router-link to="/regist">注册</router-link>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>

<style>
* {
  padding: 0;
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(124, 205, 240);
  width:1200px;
  height: 800px;
  margin: 20px auto;
  padding: 40px;
}
#nav {
    width: 300px;
    height: 500px;
    background-color: white;
    margin:15px  auto;
    border-radius: 25px;
}

#head {
    height: 50px;
    width: 300px;
    background-color:white;
    text-align: center;
    line-height: 50px;
    border: 1px solid;
    border-top-left-radius: 25px;
    border-top-right-radius: 25px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-align: left;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
