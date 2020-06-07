<!--
 * @Author: FengSiJia
 * @Date: 2020-05-26 00:02:27
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-30 23:20:11
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/ActivityManage.vue
--> 
<template>
    <el-card>
        <div id="recourse-header-title">志愿活动管理<el-button type="primary" @click="pubDialogVisible = true">发布志愿活动</el-button></div>
        <el-table
            :data="activity_list"
            style="width: 100%"
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
            label="活动状态">
            <template slot-scope="scope">
        　　　　<el-select v-model="scope.row.expired" @change="changeStatus(scope.row)">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
            </el-select>
    　　　　</template>
            </el-table-column>
            <el-table-column
            prop="activity_points"
            label="活动积分">
            </el-table-column>
            <el-table-column
            prop="date"
            label="活动时间">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100" >
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click.stop="checkDetail(scope.$index, scope.row)">删除</el-button>
                  <el-button type="text" @click.stop="checkModify(scope.row)">修改</el-button>
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

        <el-dialog
        title="志愿活动发布"
        :visible.sync="pubDialogVisible"
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
             <el-form-item label="活动积分" label-position="left">
                  <el-input v-model="pub.activity_points" placeholder="请输入活动积分"></el-input>
            </el-form-item>
             <el-form-item label="联系人" label-position="left">
                  <el-input v-model="pub.contact" placeholder="请输入活动联系人"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="pubCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="pubConfig">确 定</el-button>
        </span>
        </el-dialog>

        <el-dialog
        title="志愿活动修改"
        :visible.sync="modifyDialogVisible"
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
             <el-form-item label="活动积分" label-position="left">
                  <el-input v-model="pub.activity_points" placeholder="请输入活动积分"></el-input>
            </el-form-item>
             <el-form-item label="联系人" label-position="left">
                  <el-input v-model="pub.contact" placeholder="请输入活动联系人"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="modifyCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="modifyConfig">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                acDialogVisible: false,
                pubDialogVisible: false,
                modifyDialogVisible: false,
                row_index:'',
                acUrl: 'http://localhost:8000/api/v1/activity/',
                changeItem: {
                    activity_name: '',
                    introduction: '',
                    date: '',
                    expired: '',
                    required_num: '',
                    address:'',
                    activity_points:'',
                    contact:'',
                },
                pub: {
                    activity_name: '',
                    introduction: '',
                    date: '',
                    required_num: '',
                    address:'',
                    activity_points:'',
                    contact:'',
                    expired:'',
                },
                ac: {
                    title: '',
                    text: '',
                    time: '',
                    people: '',
                },
                activity_list: [],
                options: [{
                    value: 0,
                    label: '未过期',
                },{
                    value: 1,
                    label: '已过期',
                },{
                    value: 2,
                    label: '已完成',
                }],
            };
        },
        mounted(){
            this.axios.get(this.acUrl).then((res)=>{
                this.activity_list = res.data;
                var nowDate = new Date();
                for(var i = 0; i < this.activity_list.length; ++i) {
                }
            })
        },
        methods: {
            handleClose(done) {
                this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
            },
            isClicked(row) {
                var _this = this;
                this.axios.get(this.acUrl+ row.activity_number).then((res)=>{
                    _this.ac.title = res.data.activity_name;
                    _this.ac.text = res.data.introduction;
                    _this.ac.time = res.data.date;
                    _this.ac.people = res.data.required_num;
                })
                this.acDialogVisible = true;
            },
            acCancel() {
                this.acDialogVisible = false;
            },
            acConfig() {
                this.acDialogVisible = false;
            },
            pubConfig() {
                this.pub.expired = 0;
                this.axios.post(this.acUrl, this.pub).then((res)=>{
                    this.pubDialogVisible = false;
                })
                
            },
            pubCancel() {
                this.pubDialogVisible = false;
            },
            checkDetail(index, rows) {
                alert(rows.activity_number);
                this.axios.delete(this.acUrl+rows.activity_number).then((res)=>{
                    this.activity_list.splice(index, 1);
                })
            },
            checkModify(row) {
                this.pub.activity_name = row.activity_name;
                this.pub.introduction = row.introduction;
                this.pub.date = row.date
                this.pub.required_num = row.required_num;
                this.pub.address = row.address;
                this.pub.activity_points = row.activity_points;
                this.pub.contact = row.contact;
                this.pub.expired = row.expired;
                this.row_index = row.activity_number;
                this.modifyDialogVisible = true;
            },
            modifyCancel(){
                this.row_index = '';
                this.modifyDialogVisible = false;
            },
            modifyConfig(){
                this.axios.put(this.acUrl+this.row_index, this.pub).then((res)=>{
                    this.row_index = '';
                    this.modifyDialogVisible = false;
                })
            },
            changeStatus(row){
                this.pub.activity_name = row.activity_name;
                this.pub.introduction = row.introduction;
                this.pub.date = row.date
                this.pub.required_num = row.required_num;
                this.pub.address = row.address;
                this.pub.activity_points = row.activity_points;
                this.pub.contact = row.contact;
                this.pub.expired = row.expired;
                this.axios.put(this.acUrl + row.activity_number, this.pub).then((res)=>{
                    alert("修改活动状态成功！");
                })
            }
        }
    }
</script>