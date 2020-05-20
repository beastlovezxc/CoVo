<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:51:31
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-20 02:59:37
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/Sidebar.vue
--> 
<template>
    <div id="nav-side-bar">
        <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-menu-item index="1">
            <template slot="title">
            <i class="el-icon-location"></i>
            <span>导航一</span>
            </template>
        </el-menu-item>
        <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">导航二</span>
        </el-menu-item>
        <el-menu-item index="3">
            <i class="el-icon-document"></i>
            <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4">
            <i class="el-icon-setting"></i>
            <span slot="title">导航四</span>
        </el-menu-item>
        </el-menu>
    </div>
</template>
<script>
export default {
  data() {
    return {};
  }
};
</script>
<style>
#nav-side-bar {
    height: 800px;
    background-color: #545c64;
}
.el-menu-item.is-active {
  background-color: #303133 !important;
}
</style>