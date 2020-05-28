<!--
 * @Author: BeanCB
 * @Date: 2020-05-24 02:00:04
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 02:28:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/RecourseListManage.vue
--> 
<template>
    <el-card>
        <div id="recourse-header-title">求助活动列表<el-button type="primary" @click="dialogVisible = true">发布求助活动</el-button></div>
        <el-table
            :data="recourse_list"
            style="width: 100%"
            :row-class-name="isChoose"
            @row-click="isClicked">
            <el-table-column
            prop="index"
            label="求助活动编号">
            </el-table-column>
            <el-table-column
            prop="title"
            label="求助活动">
            </el-table-column>
            <el-table-column
            prop="time"
            label="活动时间">
            </el-table-column>
            <el-table-column
            prop="status"
            label="活动状态">
            </el-table-column>
        </el-table>
        <el-dialog
        title="发布求助信息"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="求助标题" label-position="left">
                  <el-input v-model="form.title" placeholder="请输入求助标题"></el-input>
            </el-form-item>
            <el-form-item label="求助内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="form.text" placeholder="请输入求助内容"></el-input>
            </el-form-item>

        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="dialogVisible = false">发 布</el-button>
        </span>
        </el-dialog>
        <el-dialog
        title="求助活动详情"
        :visible.sync="recourseDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="求助标题" label-position="left">
                  <el-input v-model="recour.title" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="recour.text" placeholder:disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="recour.time" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助状态" label-position="left">
                <el-select v-model="recour.status" >
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>

        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="recourseDialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="closeRecourse">确 定</el-button>
            <el-button 
            type="success" 
            @click="publishAc">发 布</el-button>
        </span>
        </el-dialog>

        <el-dialog
        title="发布志愿活动"
        :visible.sync="acDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="活动名称" label-position="left">
                  <el-input v-model="ac.title" ></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="ac.text"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="ac.time" ></el-input>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="ac.people" placeholder="请填写活动所需人数"></el-input>
            </el-form-item>

        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="acCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="acConfig">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
    
</template>
<script>
    export default {
        data() {
            return {
                dialogVisible: false,
                recourseDialogVisible: false,
                acDialogVisible: false,
                ac: {
                    title: '求助标题1',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-06-05',
                    people: '50',
                },
                options: [{
                    value: '求助中',
                    label: '求助中',
                },{
                    value: '已拒绝',
                    label: '已拒绝',
                }],
                recourse_list: [{
                    index: '1',
                    title: '求助标题1',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-06-05',
                    status: '求助中',
                },
                {
                    index: '2',
                    title: '求助标题2',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-04-05',
                    status: '求助中',
                },
                {
                    index: '3',
                    title: '求助标题3',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-07-05',
                    status: '求助中',
                },
                {
                    index: '4',
                    title: '求助标题4',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2022-03-05',
                    status: '求助中',
                },{
                    index: '5',
                    title: '求助标题5',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-08-05',
                    status: '求助中',
                }],
                form: {
                    title:'',
                    text:'',
                },
                recour: {
                    index: '1',
                    title: '求助标题1',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-06-05',
                    status: '求助中',
                }
            };
        },
        methods: {
                isChoose({row, rowIndex}) {
                    if (row.ops === '是') {
                    return 'warning-row';
                    }
                    // } else if (rowIndex === 3) {
                    // return 'success-row';
                    // }
                    return '';
                },
                handleClose(done) {
                    this.$confirm('确认关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => {});
                },
                isClicked(row) {
                    this.recourseDialogVisible = true;
                },
                closeRecourse(){
                    this.recourseDialogVisible = false;
                },
                publishAc(){
                    this.recourseDialogVisible = false;
                    this.acDialogVisible = true;

                },
                acConfig(){
                    this.acDialogVisible = false;
                },
                acCancel() {
                    this.acDialogVisible = false;
                }
            }
    }
</script>
<style>
#recourse-header-title {
    display: flex;
    text-align: left;
    justify-content: space-between;
    font-size: 2em;
}
</style>