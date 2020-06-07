<!--
 * @Author: FengSiJia
 * @Date: 2020-05-28 22:35:53
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-28 22:55:14
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/FeedbackManage.vue
--> 
<template>
    <el-card>
        <el-table
            :data="feedback_list"
            style="width: 100%"
            :row-class-name="isJoined"
            @row-click="isClicked"> <!--是否加入-->
            <!-- <el-table-column
            prop="id"
            label="求助编号">
            </el-table-column>
            <el-table-column
            prop="ac_id"
            label="活动编号">
            </el-table-column> -->
            <el-table-column
            prop="users_name.user"
            label="求助者姓名">
            </el-table-column>
            <el-table-column
            prop="activity_name.activity_name"
            label="活动名称">
            </el-table-column>
            <el-table-column
            prop="time"
            label="反馈时间">
            </el-table-column>
            <el-table-column
            prop="feedback"
            label="反馈内容"
            :show-overflow-tooltip="true">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click.stop="checkDetail(scope.$index,scope.row)">删 除</el-button>
        　　　　</template>
　      　  </el-table-column>  
        </el-table>

         <el-dialog
        title="用户活动反馈"
        :visible.sync="fbDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form >
            <!-- <el-form-item label="求助编号" label-position="left">
                  <el-input v-model="feedback.id" ></el-input>
            </el-form-item> -->
            <el-form-item label="活动编号" label-position="left">
                  <el-input v-model="feedback.ac_id" ></el-input>
            </el-form-item>
            <el-form-item label="求助者姓名" label-position="left">
                  <el-input v-model="feedback.name" ></el-input>
            </el-form-item>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="feedback.ac_name" ></el-input>
            </el-form-item>
            <el-form-item label="反馈时间" label-position="left">
                  <el-input v-model="feedback.time" ></el-input>
            </el-form-item>
            <el-form-item label="反馈内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="feedback.text"></el-input>
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
            return {
                fbDialogVisible: false,
                feedbackurl:'http://localhost:8000/api/v1/feedback/',
                feedback: {
                    id:'',
                    ac_id:'',
                    name:'',
                    time:'',
                    text:'',
                },
                feedback_list:[]
            };
        },
        mounted(){
            this.axios.get(this.feedbackurl).then((res)=>{
                this.feedback_list = res.data;
                for(var i = 0; i < this.feedback_list.length; ++i) {
                    this.feedback_list[i].time = this.feedback_list[i].time.substr(0,19).replace('T',' ')
                }
            })
        },
        methods: {
            isClicked(row) {
                // this.feedback.id = row.id;
                this.feedback.ac_id = row.activity_name.activity_number;
                this.feedback.name = row.users_name.user;
                this.feedback.ac_name = row.activity_name.activity_name;
                this.feedback.time = row.time;
                this.feedback.text = row.feedback;
                this.fbDialogVisible = true;
            },
            fbCancel() {
                this.fbDialogVisible = false;
            },
            fbConfig() {
                this.fbDialogVisible = false;
            },
            checkDetail(index,row){
                this.axios.delete(this.feedbackurl + row.users_name.user + '/' + row.feedback_id).then((res)=>{
                    alert("删除成功！");
                    this.feedback_list.splice(index,1);
                })
                
            }
        }
    }
</script>
<style>
</style>