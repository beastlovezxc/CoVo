<!--
 * @Author: BeanCB
 * @Date: 2020-05-21 23:42:34
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-06-04 23:42:25
 * @Description: file content
 * @FilePath: \Covo\frontend\src\components\Points.vue
--> 

<template>
    <el-card class="point-card">
        <div class="point-box">
            <div>
                <div class="point-font">历史积分</div>
                <div class="points-point">{{points.activity_points}}</div>
            </div>
            <div>
                <div class="point-font">剩余积分</div>
                <div class="points-point">{{points.available_points}}</div>
            </div>
        </div>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                points: {
                    activity_points:'',
                    available_points:'',
                },
            };
        },
        mounted(){
            this.points.activity_points = sessionStorage.getItem("activity_points");
            this.points.available_points = sessionStorage.getItem("available_points");
        }
    }
</script>
<style>
.el-card {
    text-align: left;
    margin: 0 0 0 0;
}
.point-font {
    font-size: 40px;
    margin: 40px;
}
.point-box {
    display: flex;
    justify-content: space-between;
    padding: 0 200px 0 200px;
}
.points-point {
    margin-left: 80px;
    font-size: 4em;
}
</style>