<!--
 * @Author: FengSiJia
 * @Date: 2020-05-19 21:10:08
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-06-04 23:13:24
 * @Description: file content
 * @FilePath: \Covo\frontend\src\views\login.vue
--> 
<template>
    <div id="nav">
        <el-container>
            <el-header class="login-header" style="font-size: 12px">
                <div id="nav-login-herder">
                    <span class="nav-login-header-span">社区志愿管理系统</span> | 登录
                </div>
            </el-header>
            <el-container>
                <el-card class="card1">
                    <h3>用户登录</h3>
                    <div id="nav-header"><span>让我们一起为爱行动</span></div>
                    <el-form ref="form" :model="model" label-width="60px">
                    <el-form-item label="用户名" label-position="left">
                        <el-input v-model="form.account" placeholder="请输入用户名"></el-input>
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
import axios from 'axios';
  export default {
    data() {
      return {
        form: {
          account: '',
          password:'',
        }
      }
    },
    methods: {
        onLogin() {
        axios.get('http://127.0.0.1:8000/api/v1/user/'+ this.form.account).then((res)=> {
        // alert(res.data.account)
        // alert(res.data.password)
        // alert(res.data.manager)
        console.log(res);
        // if (res.data.status === 0) {
        if( res.data.account == this.form.account && res.data.password == this.form.password) {
            sessionStorage.setItem("manager", res.data.manager);
            sessionStorage.setItem("account", res.data.account);
            this.$router.push({path:'/index'});
        }
        // }
        // this.$router.go({path:'/'});
      });
        },
    //   onLogin() {
    //     axios.post('http://127.0.0.1:8000/users/api/v1/auth/',this.form,{withCredentials:true}).then((res)=> {
    //     alert(res.data.msg)
    //     console.log(res);
    //     if (res.data.status === 0) {
    //         this.$router.push({path:'/index'});
    //     }
    //     // this.$router.go({path:'/'});
    //   });
    //     // this.$router.push({path:'/index'});
    //     // console.log('login!');
    //   },
      toRegist() {
          this.$router.push({path:'/regist'});
          console.log('regist!');
      }
    }
  }
</script>
<style >
#nav {
    background-color: #ededed;
    position: relative;
    background-image: "@/assets/back1.jpeg";
    /* background-repeat: "no-repeat";
    background-size: "100% 100%"; */
    /* margin: 150px auto; */
    /* padding: 150px auto; */
    /* text-align: center; */
}
.card1 {
    width: 400px;
    /* margin: 0px auto; */
    position: absolute;
    top: 50%;
    left: 70%;
    margin: 150px 0 0 -200px;
    /* margin: 150px auto; */
}
.login-header {
    background-color: white;
    box-shadow: 0 2px 5px 0px #888888;
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
    font-size: 2.5em;
    text-align: left;
}
.nav-login-header-span {
    color: #ff6a00;
    font-weight: bold;
}
</style>