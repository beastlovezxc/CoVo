<!--
 * @Author: BeanCB
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-14 00:36:40
 * @Description: file content
 * @FilePath: /Covo/frontend/src/App.vue
 -->
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">123</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
