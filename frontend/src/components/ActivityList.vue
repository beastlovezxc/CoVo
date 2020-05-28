<!--
 * @Author: BeanCB
 * @Date: 2020-05-22 00:42:34
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 01:10:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/ActivityList.vue
--> 
<template>
    <el-card>
        <el-table
            :data="activity_list"
            style="width: 100%"
            :row-class-name="isJoined"
            @row-click="isClicked"> <!--是否加入-->
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
            <el-table-column label="操作" align="center" min-width="100" prop="status">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button v-if="scope.row.status" type="text" @click="checkDetail(scope.row.phone)">已参加</el-button>
                  <el-button v-if="!scope.row.status" type="text" @click="checkDetail(scope.row.phone)">参 加</el-button>
        　　　　</template>
　      　  </el-table-column>  
        </el-table>

        <el-dialog
        title="志愿活动详情"
        :visible.sync="acDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="ac.title" disabled="true" ></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="ac.text" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="ac.time" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="ac.people" disabled="true"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="acCancel">取 消</el-button>
            <el-button 
            type="success" 
            @click="acConfig">参 加</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                acDialogVisible: false,
                ac: {
                    title:'志愿活动1',
                    text: '这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111',
                    time: '2020-06-25',
                    people: '500',
                },
                activity_list: [{
                    activity_number: '1',
                    activity_name: '志愿活动1',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020.06.20',
                    ops: '450',
                    status: true,
                    }, {
                    activity_number: '2',
                    activity_name: '志愿活动2',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020.06.21',
                    ops: '450',
                    status: false,
                    }, {
                    activity_number: '3',
                    activity_name: '志愿活动3',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020.06.23',
                    ops: '450',
                    status: false,
                    }, {
                    activity_number: '4',
                    activity_name: '志愿活动4',
                    required_num: '500',
                    participants: '450',
                    expired: '是',
                    activity_points: "150",
                    date: '2020.06.24',
                    ops: '参加',
                    status: false,
                    }]
            };
        },
        mounted() {
            let currentTime = new Date();
            var al;
            let url = 'http://localhost:8000/activity/activity';
            this.axios.get(url).then((res)=> {
                this.activity_list = res.data;
                for(var i = 0; i < this.activity_list.length; ++i){
                    // alert(this.activity_list[i].expired);
                    if( this.activity_list[i].expired === false) {
                        this.activity_list[i].expired = '否';
                    } else {
                        this.activity_list[i].expired = '是';
                    }
                }
                console.log(currentTime.getTime);
                // alert(currentTime.getTime);
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
            },
            isClicked(row){
                this.acDialogVisible = true;
            }
        }
    }
</script>