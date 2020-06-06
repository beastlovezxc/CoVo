<!--
 * @Author: BeanCB
 * @Date: 2020-05-25 23:02:50
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-06-04 01:21:01
 * @Description: file content
 * @FilePath: \Covo\frontend\src\components\UserList.vue
--> 
<template>
    <el-card>
        <el-table
            :data="volunteer_list"
            style="width: 100%"
            :row-class-name="isChange"
            @row-click="isClicked"> <!--是否加入-->
            <el-table-column
            prop="volunteer_number"
            label="用户编号">
            </el-table-column>
            <el-table-column
            prop="volunteer_name"
            label="用户姓名">
            </el-table-column>
            <el-table-column
            prop="sex"
            label="性别"
            :formatter="sexFormat">
            </el-table-column>
            <el-table-column
            prop="age"
            label="年龄">
            </el-table-column>
            <el-table-column
            prop="address"
            label="地址">
            </el-table-column>
            <el-table-column
            prop="cultural_level"
            label="文化水平">
            </el-table-column>
            <el-table-column
            prop="activity_points"
            label="活动积分">
            </el-table-column>
        </el-table>
        <el-dialog
        title="用户详细资料"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <div class="user-info"><span class="user-info-span">姓名：</span><span>{{user.volunteer_name}}</span></div>
        <div class="user-info"><span class="user-info-span">性别：</span><span>{{user.sex}}</span></div>
        <div class="user-info"><span class="user-info-span">年龄：</span><span>{{user.age}}</span></div>
        <div class="user-info"><span class="user-info-span">电话：</span><span>{{user.tel}}</span></div>
        <div class="user-info"><span class="user-info-span">住址：</span><span>{{user.address}}</span></div>
        <div class="user-info"><span class="user-info-span">文化水平：</span><span>{{user.cultural_level}}</span></div>
        <div class="user-info"><span class="user-info-span">活动积分：</span><span>{{user.activity_points}}</span></div>
        <div class="user-info"><span class="user-info-span">现有积分：</span><span>{{user.available_points}}</span></div>
        <span slot="footer" class="dialog-footer">
            <el-button 
            type="primary" 
            @click="dialogVisible = false">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                dialogVisible: false,
                usInfoUrl: 'http://127.0.0.1:8000/api/v1/volunteer/',
                form: {
                    name:'',
                    title:'',
                },
                user: {
                    volunteer_number:'',
                    volunteer_name:'',
                    sex:'',
                    age: "",
                    tel: '',
                    address: "",
                    cultural_level: '',
                    activity_points: '',
                    available_points: '',
                    users:'',
                },
                volunteer_list:[]
            };
        },
        created: function() {
            this.axios.get('http://127.0.0.1:8000/api/v1/volunteer/').then((res)=>{
                this.volunteer_list = res.data;
            })
        },
        methods: {
                isChange({row, rowIndex}) {
                    if (row.ops === '是') {
                    return 'warning-row';
                    }
                    // } else if (rowIndex === 3) {
                    // return 'success-row';
                    // }
                    return '';
                },
                isClicked(row) {
                    var _this = this;
                    this.axios.get(this.usInfoUrl + row.users).then((res)=>{
                        _this.user.volunteer_number = res.data.volunteer_number;
                        _this.user.volunteer_name = res.data.volunteer_name;
                        _this.user.sex = res.data.sex;
                        _this.user.age = res.data.age;
                        _this.user.tel = res.data.tel;
                        _this.user.address = res.data.address;
                        _this.user.cultural_level = res.data.cultural_level;
                        _this.user.activity_points = res.data.activity_points;
                        _this.user.available_points = res.data.available_points;
                        _this.user.users = res.data.users;
                        
                    })
                    this.dialogVisible = true;
                },
                handleClose(done) {
                    this.$confirm('确认关闭？')
                    .then(_ => {
                        done();
                    })
                    .catch(_ => {});
                },
                sexFormat(row, column){
                    if(row.sex) {
                        return '女';
                    } else {
                        return '男';
                    }
                }
            }
    }
</script>
<style>
.user-info {
    font-size: 2em;
}
.user-info-span {
    font-weight: bold;
}
</style>