<!--
 * @Author: BeanCB
 * @Date: 2020-05-19 21:10:08
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-20 23:28:21
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/login.vue
--> 
<template>
    <div id="nav">
        <el-container>
            <el-header>
                <div id="nav-login-herder">
                    志愿者活动管理系统 | 登录
                </div>
            </el-header>
            <el-container>
                <el-card>
                    <h3>用户登录</h3>
                    <div id="nav-header"><span>让我们一起为爱行动</span></div>
                    <el-form ref="form" :model="model" label-width="60px">
                    <el-form-item label="用户名" label-position="left">
                        <el-input v-model="form.name" placeholder="请输入用户名"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" label-position="left">
                        <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
                    </el-form-item>
                    <el-button type="primary" @click="onLogin">登录</el-button>
                    <el-button @click="toRegist">注册</el-button>
                    </el-form>
                </el-card>
            </el-container>
        </el-container>
      
    </div>
</template>
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          password:'',
        }
      }
    },
    methods: {
      onLogin() {
        this.$router.push({path:'/index'});
        console.log('login!');
      },
      toRegist() {
          this.$router.push({path:'/regist'});
          console.log('regist!');
      }
    }
  }
</script>
<style >
#nav {
    background-color: white;
    position: relative;
    /* margin: 150px auto; */
    /* padding: 150px auto; */
    /* text-align: center; */
}
.el-card {
    width: 400px;
    /* margin: 0px auto; */
    position: absolute;
    top: 50%;
    left: 70%;
    margin: 150px 0 0 -200px;
    /* margin: 150px auto; */
}
#nav-header {
    text-align: left;
    height: 40px;
    color: purple;
}
#nav-login-herder {
    height: 100px;
    width: 100%;
    line-height: 50px;
    font-size: 2em;
    text-align: left;
}
</style>