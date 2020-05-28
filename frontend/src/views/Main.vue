<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:00:36
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 02:17:36
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/Main.vue
--> 

<template>
<div>
    <el-container>
        <el-header style="font-size: 12px">
            <div id="nav-header-el">
                <div v-if="is_manage"><span>社区志愿管理系统</span> | 控制台 | 管理员</div>
                <div v-if="!is_manage"><span>社区志愿管理系统</span> | 控制台 | 普通用户</div>
                <div v-if="!is_manage"><span>活动积分：{{points.p1}} 剩余积分:{{points.p2}}</span></div>
                <div><Avatar /></div>
            </div>
            </el-header>
        <el-container>
            <el-aside>
            <Sidebar v-if="!is_manage" v-on:changeMainPage="changeMainPage1($event)"/>
            <SidebarManage v-if="is_manage" v-on:changeMainPage="changeMainPage1($event)"/>
        </el-aside>
            <el-main>
                <Information v-if="main_page === '11'"/>
                <Points v-if="main_page === '12'"/>
                <UserList v-if="main_page === '13'"/>
                <MyActivity v-if="main_page === '21'"/>
                <ActivityList v-if="main_page === '41'"/>
                <ActivityManage v-if="main_page === '42'"></ActivityManage>
                <RecourseList v-if="main_page === '51'"/>
                <MyRecourseList v-if="main_page === '52'"></MyRecourseList>
                <WalfaraManage v-if="main_page === '71'"/>
                <WalfareList v-if="main_page === '72'"/>
                <VolunteerListManage v-if="main_page === '31'"/>
                <FeedbackManage v-if="main_page === '81'"></FeedbackManage>
                <RecourseListManage v-if="main_page === '54'"></RecourseListManage>
                <MyFeedback v-if="main_page === '53'"></MyFeedback>
            </el-main>
        </el-container>
    </el-container>

</div>


</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import SidebarManage from "@/components/SidebarManage.vue";
import Headerbar from "@/components/Headerbar.vue";
import Information from "@/components/Information.vue";
import Avatar from "@/components/Avatar.vue";
import Points from "@/components/Points.vue";
import MyActivity from "@/components/MyActivity.vue";
import ActivityList from "@/components/ActivityList.vue";
import ActivityManage from "@/components/ActivityManage.vue";
import RecourseList from "@/components/RecourseList.vue";
import MyRecourseList from "@/components/MyRecourseList.vue";
import UserList from "@/components/UserList.vue";
import WalfaraManage from "@/components/WalfaraManage.vue";
import WalfareList from "@/components/WalfareList.vue";
import VolunteerListManage from "@/components/VolunteerListManage.vue"
import FeedbackManage from "@/components/FeedbackManage.vue"
import RecourseListManage from "@/components/RecourseListManage.vue"
import MyFeedback from "@/components/MyFeedback.vue"
  export default {
        data(){
            return {
                points: {
                    p1:"550",
                    p2:"450",
                },
                is_manage: true,
                main_page: "11",
            }
        },
        name:"name",
        components: {
            Sidebar,
            SidebarManage,
            Headerbar,
            Information,
            Avatar,
            Points,
            MyActivity,
            ActivityList,
            RecourseList,
            UserList,
            WalfaraManage,
            WalfareList,
            ActivityManage,
            MyRecourseList,
            VolunteerListManage,
            FeedbackManage,
            RecourseListManage,
            MyFeedback
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