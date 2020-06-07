<!--
 * @Author: FengSiJia
 * @Date: 2020-05-26 00:12:28
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-29 01:31:27
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/MyRecourseList.vue
--> 
<template>
    <el-card>
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
            <el-table-column label="操作" align="center" min-width="100" prop="status">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button  type="text" @click.stop="checkDetail(scope.$index,scope.row)">撤 销</el-button>
                  <el-button  type="text" @click.stop="checkModify(scope.$index,scope.row)">修 改</el-button>
        　　　　</template>
　      　  </el-table-column>  
        </el-table>
        <el-dialog
        title="求助信息详情"
        :visible.sync="pushDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="求助标题" label-position="left">
                  <el-input v-model="re.title" placeholder="请输入求助标题" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="re.text" 
                  placeholder="请输入求助内容"
                  disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="re.time" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助状态" label-position="left">
                <el-select v-model="re.status" disabled="falsefsdf">
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
            @click="pushDialogVisible = false">确 定</el-button>
        </span>
        </el-dialog>

        <el-dialog
        title="求助信息修改"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="求助标题" label-position="left">
                  <el-input v-model="re.title" placeholder="请输入求助标题"></el-input>
            </el-form-item>
            <el-form-item label="求助内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="re.text" placeholder="请输入求助内容"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="re.time" :disabled="false"></el-input>
            </el-form-item>
            <el-form-item label="求助状态" label-position="left">
                <el-select v-model="re.status" disabled="false">
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
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="pubConfirm">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
    
</template>
<script>
    export default {
        data() {
            return {
                dialogVisible: false,
                pushDialogVisible: false,
                url:'http://localhost:8000/api/v1/recourse/',
                account:'',
                form: {
                    name:'',
                    password:'',
                },
                re: {
                    index:'',
                    title: '',
                    text: '',
                    time:'',
                    status:'',
                    users:'',
                },
                recourse_list: [],
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
            };
        },
        mounted() {
            var _this = this;
            this.account = sessionStorage.getItem("account");
            this.axios.get(this.url+this.account).then((res)=>{
                _this.recourse_list = res.data;
                for(var i = 0; i < _this.recourse_list.length; ++i) {
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
                        _this.re.title = res.data.title;
                        _this.re.text = res.data.text;
                        _this.re.time = res.data.time;
                        _this.re.status = res.data.status;
                    })
                    this.recourseDialogVisible = true;
                    this.pushDialogVisible = true;
                },
                checkModify(index, rows) {
                    var _this = this;
                    this.axios.get(this.url+ rows.index).then((res)=>{
                        _this.re.index = res.data.index;
                        _this.re.title = res.data.title;
                        _this.re.text = res.data.text;
                        _this.re.time = res.data.time;
                        _this.re.status = res.data.status;
                    })
                    this.dialogVisible = true;
                },
                checkDetail(index, rows) {
                    var _this = this;
                    this.axios.delete(this.url+rows.index).then((res)=>{
                        alert("撤销成功！");
                    });
                    this.recourse_list.splice(index, 1);
                },
                pubConfirm(){
                    this.re.users = this.account;
                    this.axios.put(this.url+this.re.index,this.re).then((res)=>{
                        alert("更新成功！");
                    })
                    this.dialogVisible = false;
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