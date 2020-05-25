<!--
 * @Author: BeanCB
 * @Date: 2020-05-25 23:02:50
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-25 23:13:01
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/UserList.vue
--> 
<template>
    <el-card>
        <el-table
            :data="volunteer_list"
            style="width: 100%"
            :row-class-name="isJoined"> <!--是否加入-->
            <el-table-column
            prop="volunteer_number"
            label="志愿者编号">
            </el-table-column>
            <el-table-column
            prop="volunteer_name"
            label="志愿者姓名">
            </el-table-column>
            <el-table-column
            prop="sex"
            label="sex">
            </el-table-column>
            <el-table-column
            prop="age"
            label="年龄">
            </el-table-column>
            <el-table-column
            prop="address"
            label="地址">
            </el-table-column>
            <el-table-column
            prop="cultural_level"
            label="文化水平">
            </el-table-column>
            <el-table-column
            prop="activity_points"
            label="活动积分">
            </el-table-column>
           <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">同意</el-button>
        　　　　</template>
　      　 </el-table-column>  
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                volunteer_list:[{
                    volunteer_number: "1",
                    volunteer_name: "陈斌",
                    sex: "男",
                    age: "25",
                    address: "沈阳建筑大学",
                    cultural_level: "硕士",
                    activity_points: "500",
                },{
                    volunteer_number: "1",
                    volunteer_name: "陈斌",
                    sex: "男",
                    age: "25",
                    address: "沈阳建筑大学",
                    cultural_level: "硕士",
                    activity_points: "500",
                },{
                    volunteer_number: "1",
                    volunteer_name: "陈斌",
                    sex: "男",
                    age: "25",
                    address: "沈阳建筑大学",
                    cultural_level: "硕士",
                    activity_points: "500",
                },{
                    volunteer_number: "1",
                    volunteer_name: "陈斌",
                    sex: "男",
                    age: "25",
                    address: "沈阳建筑大学",
                    cultural_level: "硕士",
                    activity_points: "500",
                }]
            };
        }
    }
</script>