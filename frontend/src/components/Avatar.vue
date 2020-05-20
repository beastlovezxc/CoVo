<!--
 * @Author: BeanCB
 * @Date: 2020-05-21 00:42:31
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-21 00:44:11
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/Avatar.vue
--> 
<template>
        <div class="block"><el-avatar :size="50" :src="circleUrl"></el-avatar></div>
</template>
<script>
  export default {
    data () {
      return {
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        sizeList: ["large", "medium", "small"]
      }
    }
  }
</script>