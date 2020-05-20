<!--
 * @Author: BeanCB
 * @Date: 2020-05-13 22:52:01
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-20 02:47:34
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* width:1200px; */
  height: 800px;
  margin: 0px auto;
  /* padding: 40px; */
}

h3 {
    height: 40px;
}

</style>
