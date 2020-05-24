<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:00:36
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-24 14:56:39
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/Main.vue
--> 

<template>
<div>
    <el-container>
        <el-header style="font-size: 12px">
            <div id="nav-header-el">
                <div><span>志愿者活动管理系统</span> | 控制台</div>
                <div><Avatar /></div>
            </div>
            </el-header>
        <el-container>
            <el-aside>
            <Sidebar v-on:changeMainPage="changeMainPage1($event)"/>
        </el-aside>
            <el-main>
                <Information v-if="main_page === '11'"/>
                <Points v-if="main_page === '12'"/>
                <MyActivity v-if="main_page === '21'"/>
                <ActivityList v-if="main_page === '41'"/>
                <RecourseList v-if="main_page === '51'"/>
            </el-main>
        </el-container>
    </el-container>

</div>


</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import Headerbar from "@/components/Headerbar.vue";
import Information from "@/components/Information.vue";
import Avatar from "@/components/Avatar.vue"
import Points from "@/components/Points.vue"
import MyActivity from "@/components/MyActivity.vue"
import ActivityList from "@/components/ActivityList.vue"
import RecourseList from "@/components/RecourseList.vue"
  export default {
      data(){
          return {
          main_page: "11",
          }
      },
      name:"name",
      components: {
          Sidebar,
          Headerbar,
          Information,
          Avatar,
          Points,
          MyActivity,
          ActivityList,
          RecourseList,
      },
    methods: {
        changeMainPage1:function(index) {
            console.log(this);
            console.log(index);
            this.main_page = index;
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        }
    }
  }
</script>
<style>
/* #nav-main {
    width: 1005px;
} */
.el-aside {
    background-color: #ededed;
    width: 200px !important;    /* height: 00px; */
    /* border-top: 1px solid; */
    margin-top: 2px;
}
.el-header {
    background-color: white;
    box-shadow: 0 2px 5px 0px #888888;
}
#nav-header-el {
    height: 10px;
    width: 100%;
    line-height: 50px;
    font-size: 2.5em;
    text-align: left;
    display: flex;
    justify-content: space-between;
}
#nav-header-el span {
    color: #ff6a00;
    font-weight: bold;
}
</style>