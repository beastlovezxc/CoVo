<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:51:31
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-21 23:39:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/Sidebar.vue
--> 
<template>
    <div id="nav-side-bar">
        <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose">
        <el-submenu index="1">
            <template slot="title">
            <i class="el-icon-location"></i>
            <span>个人信息</span>
            </template>
            <el-menu-item-group>
                <el-menu-item index="1-1" v-on:click="changeMainPage('11')">基本资料</el-menu-item>
                <el-menu-item index="1-2" v-on:click="changeMainPage('12')">积分详情</el-menu-item>
            </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="2" v-on:click="changeMainPage('21')">
            <i class="el-icon-menu" ></i>
            <span slot="title" >我的活动</span>
        </el-menu-item>
        <el-menu-item index="3">
            <i class="el-icon-document"></i>
            <span slot="title">个人积分</span>
        </el-menu-item>
        <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">志愿活动</span>
        </el-menu-item>
        <el-menu-item index="5">
            <i class="el-icon-setting"></i>
            <span slot="title">报名信息</span>
        </el-menu-item>
        <el-menu-item index="6">
            <i class="el-icon-setting"></i>
            <span slot="title">我的反馈</span>
        </el-menu-item>
        <el-menu-item index="7">
            <i class="el-icon-setting"></i>
            <span slot="title">热点聚焦</span>
        </el-menu-item>
        <el-menu-item index="8">
            <i class="el-icon-setting"></i>
            <span slot="title">志愿风采</span>
        </el-menu-item>
        </el-menu>
    </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
      changeMainPage:function(index) {
          this.$emit('changeMainPage', index);
      },
  }
};
</script>
<style>
#nav-side-bar {
    height: 800px;
    width: 200px;
    background-color: #f7f4f4;
}
.el-menu-item.is-active {
  background-color: #ededed !important;
}
</style>