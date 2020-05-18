<!--
 * @Author: BeanCB
 * @Date: 2020-05-18 23:15:37
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-18 23:22:58
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/regist.vue
--> 
<template>
    <div id="login-main">
        <div class="nav-input">
            <div class="nav-text">登录名</div>
            <input v-model="account" placeholder="请输入登录名">
        </div>
        <div class="nav-input">
            <div class="nav-text">密码</div>
            <input v-model="password" placeholder="请输入密码" type="password">
        </div>
        <div class="nav-input">
            <div class="nav-text">姓名</div>
            <input v-model="password" placeholder="请输入密码">
        </div>
        <div class="nav-input">
            <div class="nav-text">性别(选填)</div>
            <input v-model="password" placeholder="请输入密码">
        </div>
        <div class="nav-input">
            <div class="nav-text">手机号</div>
            <input v-model="password" placeholder="请输入密码">
        </div>
        <div class="button">注册</div>
        <div id="nav-license">注册协议</div>
    </div>
</template>
<style>
#login-main {
    width:300px;
    height:450px;
    background-color: white;
    padding:0;
    border: 1px solid;
    border-bottom-left-radius: 25px;
    border-bottom-right-radius: 25px;
}
.nav-head-text{
    height: 80px;
    width: 300px;
    color: purple;
    line-height: 50px;
    text-align: left;
    text-indent: 1em;
}
input {
    width: 200px;
    height: 40px;
    background-color: white;
    margin: 10px 15px 0 0;
    border:1px solid #ddd;
    font-size:10px;
    border-radius: 4px;
    color:black; 
}
.nav-input {
    height: 50px;
    width: 300px;
    background-color: white;
}
.nav-text {
    float:left;
    width: 50px;
    height: 40px;
    text-align: center;
    line-height: 60px;
    background-color: white;
    margin: 10px 15px 0 15px;
}
.nav-info:empty::before {
        content: attr(placeholder);
    }
.button {
    height: 40px;
    width: 200px;
    margin: 20px auto;
    background-color: rgb(44, 243, 4);
    line-height: 40px;
    border: 1px solid;
    border-radius: 10px;
}
#nav-license {
    color:chartreuse
}
</style>