<!--
 * @Author: FengSiJia
 * @Date: 2020-05-18 23:15:37
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-20 01:28:21
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/regist.vue
--> 
<template>
    <div id="nav">
        <el-container>
            <el-header class="login-header" style="font-size: 12px">
                <div id="nav-login-herder">
                    <span class="nav-login-header-span">社区志愿管理系统</span> | 注册
                </div>
            </el-header>
            <el-container>
                <el-card class="card2">
                    <h3>用户注册</h3>
                    <el-form ref="form" :model="model" label-width="60px">
                    <el-form-item label="用户名" label-position="left">
                        <el-input v-model="form.account" placeholder="请输入用户名"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" label-position="left">
                        <el-input v-model="form.password" type="password" placeholder="请输入密码"></el-input>
                    </el-form-item>
                    <el-button type="primary" @click="toLogin">登录</el-button>
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
                form:{
                    account:'',
                    password:'',
                    manager:0,
                },
                info: {
                    volunteer_number: '',
                    volunteer_name: '',
                    sex: '',
                    age: '',
                    tel:'',
                    address:'',
                    cultural_level:'',
                    activity_points:'',
                    available_points:'',
                    users:'',
                    },
                status:'',
            }
        },
        methods: {
            toLogin(){
                this.$router.push({path:'/'});
                console.log('login!');
            },
            toRegist() {
                if( this.form.account === '' || this.form.password === '') {
                    alert('账号或密码不能为空！');
                    return;
                }

                axios.post('http://127.0.0.1:8000/api/v1/user/', this.form).catch(function(error){
                    alert(error.response.status)
                    this.status = error.response.status;
                    switch(error.response.status){
                        case 201:
                            alert("注册成功！")
                            this.$router.push({path:'/'});
                            break;
                        case 400:
                            alert("用户名已存在！");
                            
                            break;
                    }
                }).then((res)=>{
                    if (this.status !== 400) {
                        alert("注册成功！")
                        this.info.users = res.data.account;
                        this.$router.push({path:'/'});
                    }
                })
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
.card2 {
    width: 400px;
    /* margin: 0px auto; */
    position: absolute;
    top: 50%;
    left: 50%;
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