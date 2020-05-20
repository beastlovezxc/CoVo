<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:00:36
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-21 00:56:19
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/Main.vue
--> 

<template>
<div>
    <el-container style="height: 800px; border: 1px solid">
        <el-header style="font-size: 12px">
            <div id="nav-header-el">
                <div><span>志愿者活动管理系统</span> | 控制台</div>
                <div><Avatar/></div>
            </div>
            </el-header>
        <el-container>
            <el-aside>
            <Sidebar/>
        </el-aside>
            <el-main>
                <Information/>
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
  export default {
      name:"name",
      components: {
          Sidebar,
          Headerbar,
          Information,
          Avatar,
      },
    methods: {
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