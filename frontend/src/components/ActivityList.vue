<!--
 * @Author: FengSiJia
 * @Date: 2020-05-22 00:42:34
 * @LastEditors: FengSiJia
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
            label="活动状态">
            <template slot-scope="scope">
        　　　　<el-select v-model="scope.row.expired" :disabled=true>
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
            <el-table-column label="操作" align="center" min-width="100" prop="status">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button v-if="scope.row.status" type="text" @click.stop="acConfig(scope.row)">已参加</el-button>
                  <el-button v-if="!scope.row.status" type="text" @click.stop="acConfig(scope.row)">参 加</el-button>
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
                  <el-input v-model="ac.activity_name" disabled="true" ></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="ac.introduction" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="ac.date" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="ac.required_num" disabled="true"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="acCancel">取 消</el-button>
            <el-button 
            type="success" 
            @click="acConfig2">参 加</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                acDialogVisible: false,
                root:'',
                url: 'http://localhost:8000/api/v1/activity/',
                formurl:'http://localhost:8000/api/v1/applicationform/',
                voInfoUrl:'http://localhost:8000/api/v1/volunteer/',
                ac: {
                    activity_number:'',
                    activity_name:'',
                    introduction: '',
                    expired:'',
                    date: '',
                    required_num: '',
                    participants:'',
                    address:'',
                    activity_points:'',
                    contact:'',
                },
                form: {
                    account:'',
                    activity_number:'',
                    voinfo:'',
                    status: '',
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
        mounted() {
            this.root = sessionStorage.getItem("account");
            let currentTime = new Date();
            var al;
            let url = 'http://localhost:8000/api/v1/activity/';
            this.axios.get(url).then((res)=> {
                this.activity_list = res.data;
                for(var i = 0; i < this.activity_list.length; ++i){
                    // alert(this.activity_list[i].expired);
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
                var _this = this;
                this.axios.get(this.url+row.activity_number).then((res)=>{
                    // alert(res.data.activity_name);
                    _this.ac.activity_number = res.data.activity_number;
                    _this.ac.activity_name = res.data.activity_name;
                    _this.ac.introduction = res.data.introduction;
                    _this.ac.required_num = res.data.required_num;
                    _this.ac.date = res.data.date;
                })
                this.acDialogVisible = true;
            },
            acCancel() {
                this.acDialogVisible = false;
            },
            async getConfirmAjax(rows){
                var _this = this;
                var status = 404;
                await this.axios.get(this.formurl + this.root+'/activity/' + rows.activity_number).then((res)=>{
                    status = res.status;
                    // return status;
                }).catch(function(error){
                    return status;
                })
                return status;
            },
            async getVoInfoAjax() {
                var _this = this;
                await this.axios.get(_this.voInfoUrl+_this.root).then((Res)=>{
                    _this.form.voinfo = Res.data.volunteer_number;
                });
            },
            async postApAjax(){
                var _this = this;
                this.form.status = '0';
                await _this.axios.post(_this.formurl,_this.form).then((Res)=>{
                    if(Res.status === 201) {
                        alert("报名成功！");
                    }
                });
            },
            async acConfig(rows){
                var _this = this;
                if (rows.expired === 1) {
                    alert("活动已过期，无法报名！");
                    return;
                } else if (rows.expired === 2) {
                    alert("活动已结束，无法报名！");
                    return;
                }
                var status = await this.getConfirmAjax(rows);
                if (status === 404) {
                    this.form.account = this.root;
                    this.form.activity_number = rows.activity_number;
                    await this.getVoInfoAjax();
                    await this.postApAjax();
                } else {
                    alert("您已经报名此活动!");
                }
            },
            // acConfig(rows) {
            //     var _this = this;
            //     this.axios.get(this.formurl + this.root+'/activity/' + rows.activity_number).
            //     catch(function(error){
            //         _this.form.account = _this.root;
            //         _this.form.activity_number = rows.activity_number;
            //         _this.axios.get(_this.voInfoUrl+_this.root).then((mRes)=>{
            //             _this.form.voinfo = mRes.data.volunteer_number;
            //         });
            //         _this.axios.post(_this.formurl,_this.form).then((mRes)=>{
            //             if(mRes.status === 201) {
            //                 alert("报名成功！");
            //             }
            //         });
            //     }).then((res)=>{
            //         if(res.status === 200) {
            //             alert("您已经报名此活动！");
            //         }
            //     })
            // },
            acConfig2(){
                var _this = this;
                this.axios.get(this.formurl + this.root+'/activity/' + _this.ac.activity_number).
                catch(function(error){
                    _this.form.account = _this.root;
                    _this.form.activity_number = _this.ac.activity_number;
                    _this.axios.post(_this.formurl,_this.form).then((mRes)=>{
                        if(mRes.status === 201) {
                            alert("报名成功！");
                        }
                    })
                }).then((res)=>{
                    if(res.status === 200) {
                        alert("您已经报名此活动！");
                    }
                })
            }
        }
    }
</script>
<style>

</style>