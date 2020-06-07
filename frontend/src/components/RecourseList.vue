<!--
 * @Author: FengSiJia
 * @Date: 2020-05-29 01:13:20
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-29 01:17:47
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/RecourseList.vue
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
            <template slot-scope="scope">
                 <el-select v-model="scope.row.status" disabled="true">
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
            <el-date-picker
                v-model="form.time"
                type="datetime"
                placeholder="选择日期时间"
                align="right"
                :picker-options="pickerOptions">
            </el-date-picker>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="pubRecourse">发 布</el-button>
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
                  v-model="recour.text" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="recour.time" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助状态" label-position="left">
                <el-select v-model="recour.status" disabled="true">
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
            <el-button 
            type="primary" 
            @click="closeRecourse">确 定</el-button>
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
                url:'http://localhost:8000/api/v1/recourse/',
                ac: {
                    title: '求助标题1',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-06-05',
                    people: '50',
                },
                options: [{
                    value: 0,
                    label: '求助中',
                },{
                    value: 1,
                    label: '已完成',
                },
                {
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
        mounted(){
            this.form.users = sessionStorage.getItem("account");
            this.axios.get('http://localhost:8000/api/v1/recourse/').then((res)=>{
                this.recourse_list = res.data;
                for(var i = 0; i < this.recourse_list.length; ++i) {
                    this.recourse_list[i].time = this.recourse_list[i].time.substr(0,19).replace('T',' ');
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
                    this.axios.get(this.url+ row.index).then((res)=>{
                        _this.recour.title = res.data.title;
                        _this.recour.text = res.data.text;
                        _this.recour.time = res.data.time;
                        _this.recour.status = res.data.status;
                    })
                    this.recourseDialogVisible = true;
                },
                closeRecourse(){
                    this.recourseDialogVisible = false;
                },
                publishAc(){
                    this.recourseDialogVisible = false;
                    this.acDialogVisible = true;

                },
                pubRecourse() {
                    // alert(this.form.title);
                    // alert(this.form.text);
                    // alert(this.form.time);
                    this.axios.post(this.url,this.form).then((res)=>{
                        alert("success");
                    })
                    this.dialogVisible = false;
                },
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