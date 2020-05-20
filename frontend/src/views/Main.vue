<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 01:00:36
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-20 02:53:01
 * @Description: file content
 * @FilePath: /Covo/frontend/src/views/Main.vue
--> 

<template>
<div>
    <el-container style="height: 800px; border: 1px solid #eee">
        <el-aside>
            <Sidebar/>
        </el-aside>
        <el-container>
            <el-header style="text-align: right; font-size: 12px">
            </el-header>
            <el-main>123</el-main>
        </el-container>
    </el-container>

</div>


</template>

<script>
import Sidebar from "@/components/Sidebar.vue";
import Headerbar from "@/components/Headerbar.vue";
  export default {
      name:"name",
      components: {
          Sidebar,
          Headerbar,
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
    background-color: #545c64;
    /* height: 00px; */
}
</style>