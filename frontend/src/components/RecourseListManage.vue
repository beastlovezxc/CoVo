<!--
 * @Author: FengSiJia
 * @Date: 2020-05-24 02:00:04
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-29 02:28:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/RecourseListManage.vue
--> 
<template>
    <el-card>
        <div id="recourse-header-title">求助活动列表</div>
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
            <template slot-scope="scope">
        　　　　<el-select v-model="scope.row.status" @change="changeStatus(scope.row)">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
            </el-select>
    　　　　</template>
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
                  v-model="recour.text" 
                  placeholder:disabled="true"
                  :disabled="true"></el-input>
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
                  <el-input v-model="pub.activity_name" placeholder="请输入活动名称"></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  placeholder="请输入活动介绍"
                  v-model="pub.introduction"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-date-picker
                    v-model="pub.date"
                    type="datetime"
                    placeholder="选择日期时间"
                    align="right"
                    :picker-options="pickerOptions">
                </el-date-picker>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="pub.required_num" placeholder="请填写活动所需人数"></el-input>
            </el-form-item>
             <el-form-item label="活动地址" label-position="left">
                  <el-input v-model="pub.address" placeholder="请输入活动地址"></el-input>
            </el-form-item>
             <el-form-item label="需求人数" label-position="left">
                  <el-input v-model="pub.activity_points" placeholder="请输入需求人数"></el-input>
            </el-form-item>
             <el-form-item label="联系人" label-position="left">
                  <el-input v-model="pub.contact" placeholder="请输入活动联系人"></el-input>
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
                row_index: '',
                recourseUrl:'http://localhost:8000/api/v1/recourse/',
                acUrl: 'http://localhost:8000/api/v1/activity/',
                ac: {
                    title: '',
                    text: '',
                    time: '',
                    people: '',
                },
                pub: {
                    activity_name: '',
                    introduction: '',
                    date: '',
                    required_num: '',
                    address:'',
                    activity_points:'',
                    contact:'',
                },
                options: [{
                    value: 0,
                    label: '求助中',
                },{
                    value: 1,
                    label: '已完成',
                },{
                    value: 2,
                    label: '已拒绝',
                }],
                recourse_list: [],
                form: {
                    title:'',
                    text:'',
                    time:'',
                    users:'',
                    status:'0',
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
        mounted() {
            this.axios.get(this.recourseUrl).then((res)=>{
                this.recourse_list = res.data;
                for(var i = 0; i < this.recourse_list.length; ++i){
                    // alert(this.activity_list[i].expired);
                    this.recourse_list[i].time = this.recourse_list[i].time.slice(0,19).replace('T', ' ');

                }
            })
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
                    var _this = this;
                    this.row_index = row;
                    this.axios.get(this.recourseUrl + row.index).then((res)=>{
                        this.recour.index = res.data.index;
                        this.recour.title = res.data.title;
                        this.recour.text = res.data.text;
                        this.recour.time = res.data.time;
                        this.recour.status = res.data.status;
                        this.recourseDialogVisible = true;
                    })
                    
                },
                closeRecourse(){
                    this.recourseDialogVisible = false;
                },
                publishAc(){
                    this.pub.activity_name = this.row_index.title;
                    this.pub.introduction = this.row_index.text;
                    this.pub.time = this.row_index.time;
                    this.recourseDialogVisible = false;
                    this.acDialogVisible = true;

                },
                acConfig(){
                    this.axios.post(this.acUrl, this.pub).then((res)=>{
                        this.acDialogVisible = false;
                    })
                },
                acCancel() {
                    this.acDialogVisible = false;
                },
                changeStatus(row){
                    this.form.title = row.title;
                    this.form.text = row.text;
                    // time = row.time;
                    this.form.users = row.users;
                    this.form.status = row.status;
                    this.axios.put(this.recourseUrl + row.index, this.form).then((res)=>{
                        alert('操作成功！');
                })
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