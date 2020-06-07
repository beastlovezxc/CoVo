<!--
 * @Author: FengSiJia
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-28 20:41:21
 * @Description: file content
 * @FilePath: /Covo/frontend/src/App.vue
 -->
 <!--
<template>
  <div id="app">
    <div id="nav">
      <div id="head">
        <router-link to="/">登录</router-link>  |
        <router-link to="/about">注册</router-link>
      </div>
      <router-view></router-view>
    </div>
  </div>
</template>
-->
<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          password: '',
        }
      }
    },
    methods: {
      onSubmit() {
        this.$router.push({path:'/index'});
        console.log('submit!');
      }
    }
  }
</script>
<style>
* {
  padding: 0;
  margin: 0;
}
#app {
  background-image: "./assets/back1.jpeg";
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* width:1200px; */
  /* height: 800px; */
  margin: 0px auto;
  background-color: #ededed;
  /* padding: 40px; */
}

h3 {
    height: 40px;
}
.el-table tbody tr:hover>td { 
    color: rgb(255, 124, 2);
    font-weight: bold;
    font-size: 1.5em;
    background-color:#0e77ee!important
}
</style>
