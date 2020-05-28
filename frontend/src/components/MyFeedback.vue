<!--
 * @Author: BeanCB
 * @Date: 2020-05-29 01:32:24
 * @LastEditors: BeanCB
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
            <el-table-column
            prop="id"
            label="求助编号">
            </el-table-column>
            <el-table-column
            prop="ac_id"
            label="活动编号">
            </el-table-column>
            <el-table-column
            prop="ac_name"
            label="活动名称">
            </el-table-column>
            <el-table-column
            prop="time"
            label="反馈时间">
            </el-table-column>
            <el-table-column
            prop="text"
            label="反馈内容"
            :show-overflow-tooltip="true">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">删 除</el-button>
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
            <el-form-item label="求助编号" label-position="left">
                  <el-input v-model="feedback.id" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动编号" label-position="left">
                  <el-input v-model="feedback.ac_id" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="feedback.ac_name" disabled="true"></el-input>
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
                  v-model="feedback.text"
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
            <el-form-item label="求助编号" label-position="left">
                  <el-input v-model="feedback.id" ></el-input>
            </el-form-item>
            <el-form-item label="活动编号" label-position="left">
                  <el-input v-model="feedback.ac_id" ></el-input>
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
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="feedback.text"></el-input>
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
                feedback: {
                    id:'',
                    ac_id:'',
                    name:'',
                    time:'',
                    text:'',
                },
                feedback_list:[{
                    id:'1',
                    ac_id:'1',
                    ac_name:'志愿活动1',
                    time: '2020-06-24',
                    text:'志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1志愿活动1',
                },{
                    id:'2',
                    ac_id:'2',
                    ac_name:'志愿活动2',
                    time:'2020-06-25',
                    text:'这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好这个活动做的真好',
                }],
            };
        },
        methods: {
            isClicked(row) {
                this.feedback.id = row.id;
                this.feedback.ac_id = row.ac_id;
                this.feedback.ac_name = row.ac_name;
                this.feedback.time = row.time;
                this.feedback.text = row.text;
                this.fbDialogVisible = true;
            },
            fbCancel() {
                this.fbDialogVisible = false;
            },
            fbConfig() {
                this.fbDialogVisible = false;
            },
            checkModify(rows) {
                this.feedback.id = rows.id;
                this.feedback.ac_id = rows.ac_id;
                this.feedback.ac_name = rows.ac_name;
                this.feedback.time = rows.time;
                this.feedback.text = rows.text;
                this.pushDialogVisible = true;
            },
            pushCancel() {
                this.pushDialogVisible = false;
            },
            pushConfig() {
                this.pushDialogVisible = false;
            },
        }
    }
</script>