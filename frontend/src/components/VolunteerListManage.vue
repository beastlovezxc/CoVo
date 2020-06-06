<!--
 * @Author: BeanCB
 * @Date: 2020-05-28 21:42:16
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-28 22:33:36
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/VolunteerListManage.vue
--> 
<template>
    <el-card>
        <el-table
            :data="recruit_list"
            style="width: 100%"
            @row-click="isClicked"> <!--是否加入-->
            <el-table-column
            prop="apply_id"
            label="招募编号">
            </el-table-column>
            <el-table-column
            prop="voinfo_name.volunteer_name"
            label="用户名">
            </el-table-column>
            <el-table-column
            prop="voinfo_name.sex"
            label="用户性别"
            :formatter="sexFormat">
            </el-table-column>
            <el-table-column
            prop="voinfo_name.age"
            label="用户年龄">
            </el-table-column>
            <el-table-column
            prop="activity_name.activity_number"
            label="活动编号">
            </el-table-column>
            <el-table-column
            prop="activity_name.activity_name"
            label="活动名称">
            </el-table-column>
            <el-table-column
            prop="activity_name.date"
            label="活动时间">
            </el-table-column>
            <el-table-column 
            prop="status"
            label="操作" 
            align="center" 
            min-width="100">
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
        title="用户详细资料"
        :visible.sync="userDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form :inline="true">
        <el-form-item label="姓名：" label-position="left">
                  <el-input v-model="user.name" :disabled="true"></el-input>
        </el-form-item>
        <div style="">
        <el-form-item label="性别：" label-position="left">
                  <el-input v-model="user.sex" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="年龄：" label-position="left">
                  <el-input v-model="user.age" :disabled="true"></el-input>
        </el-form-item></div>
        <el-form-item label="电话：" label-position="left">
                  <el-input v-model="user.tel" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="住址：" label-position="left">
                  <el-input v-model="user.address" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="文化水平：" label-position="left">
                  <el-input v-model="user.cultural_level" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="活动积分：" label-position="left">
                  <el-input v-model="user.activity_points" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="现有积分：" label-position="left">
                  <el-input v-model="user.available_points" :disabled="true"></el-input>
        </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button 
            type="primary" 
            @click="userDialogVisible = false">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                userDialogVisible: false,
                apInfoUrl:'http://localhost:8000/api/v1/applicationform/',
                options: [{
                    value: 0,
                    label: '申请中',
                },{
                    value: 1,
                    label: '已同意',
                },{
                    value: 2,
                    label: '已拒绝',
                }],
                user: {
                    name:'',
                    sex:'',
                    age: "",
                    tel: '',
                    address: "",
                    cultural_level: '',
                    activity_points: '',
                    available_points: '',
                },
                putUser:{
                    account:'',
                    activity_number:'',
                    voinfo:'',
                    status:'',
                    apply_id:'',
                },
                recruit_list: [],
            };
        },
        mounted() {
            this.axios.get(this.apInfoUrl).then((res)=>{
                this.recruit_list = res.data;
            })
        },
        methods: {
            isClicked(row) {
                var _this = this;
                this.axios.get(this.apInfoUrl+row.users_name.user+'/activity/' + row.activity_name.activity_number).then((res)=>{
                    _this.user.name = res.data.voinfo_name.volunteer_name;
                    _this.user.sex = res.data.voinfo_name.sex;
                    _this.user.age = res.data.voinfo_name.age;
                    _this.user.tel = res.data.voinfo_name.tel;
                    _this.user.address = res.data.voinfo_name.address;
                    _this.user.cultural_level = res.data.voinfo_name.cultural_level;
                    _this.user.activity_points = res.data.voinfo_name.activity_points;
                    _this.user.available_points = res.data.voinfo_name.available_points;
                    this.userDialogVisible = true;
                })
                
            },
            sexFormat(row, column){
                if(row.voinfo_name.sex) {
                        return '女';
                    } else {
                        return '男';
                    }
            },
            changeStatus(row) {
                this.putUser.account = row.users_name.user;
                this.putUser.activity_number = row.activity_name.activity_number;
                this.putUser.voinfo = row.voinfo_name.volunteer_number;
                this.putUser.status = row.status;
                this.axios.put(this.apInfoUrl + this.putUser.account + '/activity/' + this.putUser.activity_number, this.putUser).then((res)=>{
                    alert('操作成功！');
                })
            }
        }
    }
</script>
<style>
</style>