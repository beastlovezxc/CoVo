<!--
 * @Author: BeanCB
 * @Date: 2020-05-26 00:02:27
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-26 00:04:09
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/ActivityManage.vue
--> 
<template>
    <el-card>
        <el-table
            :data="activity_list"
            style="width: 100%"
            :row-class-name="isJoined"> <!--是否加入-->
            <el-table-column
            prop="activity_number"
            label="活动编号">
            </el-table-column>
            <el-table-column
            prop="activity_name"
            label="活动名称">
            </el-table-column>
            <el-table-column
            prop="required_num"
            label="活动所需人数">
            </el-table-column>
            <el-table-column
            prop="participants"
            label="参加人数">
            </el-table-column>
            <el-table-column
            prop="expired"
            label="是否过期">
            </el-table-column>
            <el-table-column
            prop="activity_points"
            label="活动积分">
            </el-table-column>
            <el-table-column
            prop="date"
            label="活动时间">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">删除</el-button>
                  <el-button type="text" @click="checkDetail(scope.row.phone)">修改</el-button>
        　　　　</template>
　      　  </el-table-column>  
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {

            };
        }
    }
</script>