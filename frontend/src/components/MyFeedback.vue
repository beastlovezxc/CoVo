<!--
 * @Author: FengSiJia
 * @Date: 2020-05-29 01:32:24
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-29 02:13:01
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/MyFeedback.vue
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
            </el-table-column> -->
            <el-table-column
            prop="activity_name.activity_number"
            label="活动编号">
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
                  <el-button type="text" @click.stop="checkModify(scope.row)">修 改</el-button>
        　　　　</template>
　      　  </el-table-column>  
        </el-table>

         <el-dialog
        title="用户活动反馈"
        :visible.sync="fbDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <!-- <el-form-item label="求助编号" label-position="left">
                  <el-input v-model="feedback.id" disabled="true"></el-input>
            </el-form-item> -->
            <el-form-item label="活动编号" label-position="left">
                  <el-input v-model="feedback.activity_number" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="feedback.activity_name" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="反馈时间" label-position="left">
                  <el-input v-model="feedback.time" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="反馈内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="feedback.feedback"
                  disabled="true"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button 
            type="primary" 
            @click="fbConfig">确 定</el-button>
        </span>
        </el-dialog>

        <el-dialog
        title="活动反馈修改"
        :visible.sync="pushDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form >
            <!-- <el-form-item label="求助编号" label-position="left">
                  <el-input v-model="feedback.id" ></el-input>
            </el-form-item> -->
            <el-form-item label="活动编号" label-position="left">
                  <el-input v-model="feedback.activity_number" ></el-input>
            </el-form-item>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="feedback.activity_name" ></el-input>
            </el-form-item>
            <!-- <el-form-item label="反馈时间" label-position="left">
                <el-date-picker
                v-model="feedback.time"
                type="datetime"
                placeholder="选择日期时间"
                align="right"
                :picker-options="pickerOptions">
            </el-date-picker> -->
            <!-- </el-form-item> -->
            <el-form-item label="反馈内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="feedback.feedback"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="pushCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="pushConfig">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                fbDialogVisible: false,
                pushDialogVisible: false,
                root:'',
                feedbackurl:'http://localhost:8000/api/v1/feedback/',
                feedback: {
                    feedback_id:'',
                    activity_number:'',
                    activity_name:'',
                    time:'',
                    feedback:'',
                    account:'',
                },
                feedback_list:[],
            };
        },
        mounted(){
            this.root = sessionStorage.getItem("account");
            this.axios.get(this.feedbackurl+this.root).then((res)=>{
                this.feedback_list = res.data;
            })
        },
        methods: {
            isClicked(row) {
                this.feedback.feedback_id = row.feedback_id;
                this.feedback.activity_number = row.activity_name.activity_number;
                this.feedback.activity_name = row.activity_name.activity_name;
                this.feedback.time = row.time;
                this.feedback.feedback = row.feedback;
                this.feedback.account = row.users_name.user;
                this.fbDialogVisible = true;
            },
            fbCancel() {
                this.fbDialogVisible = false;
            },
            fbConfig() {
                this.fbDialogVisible = false;
            },
            checkDetail(index,row){
                 var _this = this;
                this.axios.delete(this.feedbackurl+this.root + '/' + row.feedback_id).then((res)=>{
                    alert("删除成功！");
                });
                this.feedback_list.splice(index, 1);
            },
            checkModify(row) {
                this.feedback.feedback_id = row.feedback_id;
                this.feedback.activity_number = row.activity_name.activity_number;
                this.feedback.activity_name = row.activity_name.activity_name;
                this.feedback.time = row.time;
                this.feedback.feedback = row.feedback;
                this.feedback.account = this.root;
                this.feedback.feedback_id = row.feedback_id;
                this.pushDialogVisible = true;
            },
            pushCancel() {
                this.pushDialogVisible = false;
            },
            pushConfig() {
                var _this = this;
                this.axios.put(this.feedbackurl+this.root + '/'+this.feedback.feedback_id, this.feedback).then((res)=>{
                    alert("修改成功!");
                });
                this.pushDialogVisible = false;
            },
        }
    }
</script>