<!--
 * @Author: BeanCB
 * @Date: 2020-05-22 00:42:34
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-25 01:15:41
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/ActivityList.vue
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
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">参加</el-button>
        　　　　</template>
　      　 </el-table-column>  
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                activity_list: [{
                    activity_number: '1',
                    activity_name: '志愿活动1',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020.04.02',
                    ops: '450',
                    }, {
                    activity_number: '2',
                    activity_name: '志愿活动2',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '500',
                    ops: '450',
                    }, {
                    activity_number: '3',
                    activity_name: '志愿活动3',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '500',
                    ops: '450',
                    }, {
                    activity_number: '4',
                    activity_name: '志愿活动4',
                    required_num: '500',
                    participants: '450',
                    expired: '是',
                    activity_points: "150",
                    date: '500',
                    ops: '参加',
                    }]
            };
        },
        mounted() {
            let url = 'http://localhost:8000/activity/activity';
            this.axios.get(url).then((res)=> {
                this.activity_list = res.data;
            });
        },
        methods: {
            isJoined({row, rowIndex}) {
                if (row.ops === '是') {
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