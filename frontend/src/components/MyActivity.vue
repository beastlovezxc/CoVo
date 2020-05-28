<!--
 * @Author: BeanCB
 * @Date: 2020-05-22 00:13:55
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 01:00:43
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/MyActivity.vue
--> 
<template>
    <el-card>
          <el-table
            :data="activity_info"
            style="width: 100%"
            :row-class-name="isExpired"
            @row-click="isClicked"> <!--过期-->
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
            <el-table-column
            prop="date"
            label="活动时间">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click.stop="feedback(scope.row.phone)">发布反馈</el-button>
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
            type="primary" 
            @click="acConfig">确 定</el-button>
        </span>
        </el-dialog>

        <el-dialog
        title="发布反馈"
        :visible.sync="fbDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="反馈内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="fb.text" ></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="fbCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="fbConfig">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return{
                fbDialogVisible: false,
                acDialogVisible: false,
                fb: {
                  text:'',
                },
                ac: {
                    title:'志愿活动1',
                    text: '这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111',
                    time: '2020-06-25',
                    people: '500',
                },
                activity_info: [{
                    activity_number: '1',
                    activity_name: '志愿活动1',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020-06-25'
                    }, {
                    activity_number: '2',
                    activity_name: '志愿活动2',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020-06-25'
                    }, {
                    activity_number: '3',
                    activity_name: '志愿活动3',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020-06-25'
                    }, {
                    activity_number: '4',
                    activity_name: '志愿活动4',
                    required_num: '500',
                    participants: '450',
                    expired: '是',
                    activity_points: "150",
                    date: '2020-05-25'
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
            },
            isClicked(row)  {
                this.acDialogVisible = true;
            },
            acCancel() {
                this.acDialogVisible = false;
            },
            acConfig() {
              this.acDialogVisible = false;
            },
            feedback() {
              this.fbDialogVisible = true;
            },
            fbConfig() {
              this.fbDialogVisible = false;
            },
            fbCancel() {
              this.fbDialogVisible = false;
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