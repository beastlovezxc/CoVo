<!--
 * @Author: BeanCB
 * @Date: 2020-05-22 00:13:55
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-22 00:37:17
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/MyActivity.vue
--> 
<template>
    <el-card>
          <el-table
            :data="activity_info"
            style="width: 100%"
            :row-class-name="isExpired"> <!--过期-->
            <el-table-column
            prop="activity_number"
            label="活动编号"
            width="180">
            </el-table-column>
            <el-table-column
            prop="activity_name"
            label="活动名称"
            width="180">
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
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return{
                activity_info: [{
                    activity_number: '1',
                    activity_name: '志愿活动1',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    }, {
                    activity_number: '2',
                    activity_name: '志愿活动2',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    }, {
                    activity_number: '3',
                    activity_name: '志愿活动3',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    }, {
                    activity_number: '4',
                    activity_name: '志愿活动4',
                    required_num: '500',
                    participants: '450',
                    expired: '是',
                    activity_points: "150",
                    }]
            };
        },
        methods: {
            isExpired({row, rowIndex}) {
                if (row.expired === '是') {
                return 'warning-row';
                }
                // } else if (rowIndex === 3) {
                // return 'success-row';
                // }
                return '';
            }
            }
    }
</script>

<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
</style>