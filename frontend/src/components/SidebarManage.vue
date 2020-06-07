<!--
 * @Author: FengSiJia
 * @Date: 2020-05-26 00:57:23
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-29 01:16:40
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/SidebarManage.vue
--> 
<!--
 * @Author: FengSiJia
 * @Date: 2020-05-20 01:51:31
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-26 00:16:10
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
            <i class="el-icon-info"></i>
            <span>个人信息</span>
            </template>
            <el-menu-item-group>
                <el-menu-item index="1-3" v-on:click="changeMainPage('13')">用户列表</el-menu-item>
            </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="3" v-on:click="changeMainPage('31')">
            <i class="el-icon-sort"></i>
            <span slot="title" >招募管理</span>
        </el-menu-item>
        <!-- <el-menu-item index="2" v-on:click="changeMainPage('21')">
            <i class="el-icon-menu" ></i>
            <span slot="title" >我的活动</span>
        </el-menu-item> -->
        <!-- <el-menu-item index="3">
            <i class="el-icon-document"></i>
            <span slot="title">个人积分</span>
        </el-menu-item> -->
        <el-submenu index="4">
            <template slot="title">
            <i class="el-icon-news"></i>
            <span slot="title">志愿活动</span>
            </template>
            <!-- <el-menu-item index="4-1" v-on:click="changeMainPage('41')">志愿活动列表</el-menu-item> -->
            <el-menu-item index="4-2" v-on:click="changeMainPage('42')">志愿活动管理</el-menu-item>
        </el-submenu>
        <el-submenu index="5">
            <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">求助信息</span>
            </template>
            <el-menu-item-group>
                <el-menu-item index="5-1" v-on:click="changeMainPage('54')">求助列表</el-menu-item>
                <!-- <el-menu-item index="5-2" v-on:click="changeMainPage('52')">我的求助</el-menu-item>
                <el-menu-item index="5-3" v-on:click="changeMainPage('53')">我的反馈</el-menu-item> -->
            </el-menu-item-group>
        </el-submenu>
        <!-- <el-menu-item index="6">
            <i class="el-icon-setting"></i>
            <span slot="title">我的反馈</span>
        </el-menu-item> -->
        <el-submenu index="7">
            <template slot="title">
            <i class="el-icon-star-on"></i>
            <span slot="title">志愿福利</span>
            </template>
                <el-menu-item index="7-1" v-on:click="changeMainPage('71')">福利管理</el-menu-item>
                <!-- <el-menu-item index="7-2" v-on:click="changeMainPage('72')">福利列表</el-menu-item> -->
        </el-submenu>
        <el-menu-item index="8" v-on:click="changeMainPage('81')">
            <i class="el-icon-rank"></i>
            <span slot="title">活动反馈</span>
        </el-menu-item>
        <el-menu-item index="9">
            <i class="el-icon-view"></i>
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