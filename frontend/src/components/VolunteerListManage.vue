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
            prop="id"
            label="招募编号">
            </el-table-column>
            <el-table-column
            prop="name"
            label="用户名">
            </el-table-column>
            <el-table-column
            prop="sex"
            label="用户性别">
            </el-table-column>
            <el-table-column
            prop="age"
            label="用户年龄">
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
            prop="date"
            label="活动时间">
            </el-table-column>
            <el-table-column 
            prop="status"
            label="操作" 
            align="center" 
            min-width="100">
    　　　　<template slot-scope="scope">
        　　　　<el-select v-model="scope.row.status">
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
        <!-- <div class="user-info"><span class="user-info-span">姓名：</span><span>{{user.name}}</span></div>
        <div class="user-info"><span class="user-info-span">性别：</span><span>{{user.sex}}</span></div>
        <div class="user-info"><span class="user-info-span">年龄：</span><span>{{user.age}}</span></div>
        <div class="user-info"><span class="user-info-span">电话：</span><span>{{user.tel}}</span></div>
        <div class="user-info"><span class="user-info-span">住址：</span><span>{{user.address}}</span></div>
        <div class="user-info"><span class="user-info-span">文化水平：</span><span>{{user.cultural_level}}</span></div>
        <div class="user-info"><span class="user-info-span">活动积分：</span><span>{{user.activity_points}}</span></div>
        <div class="user-info"><span class="user-info-span">现有积分：</span><span>{{user.available_points}}</span></div> -->
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
                userDialogVisible: true,
                options: [{
                    value: '申请中',
                    label: '申请中',
                },{
                    value: '已同意',
                    label: '已同意',
                },{
                    value: '已拒绝',
                    label: '已拒绝',
                }],
                user: {
                    name:'李二',
                    sex:'男',
                    age: "24",
                    tel: '13942382772',
                    address: "沈阳建筑大学",
                    cultural_level: '硕士',
                    activity_points: '450',
                    available_points: '500',
                },
                recruit_list: [{
                    id:'1',
                    name:'李二',
                    sex:'男',
                    age:'24',
                    ac_id:'1',
                    ac_name:'志愿活动1',
                    date:'2020-06-24',
                    status:'申请中',
                },{
                    id:'2',
                    name:'李三',
                    sex:'男',
                    age:'24',
                    ac_id:'1',
                    ac_name:'志愿活动1',
                    date:'2020-06-24',
                    status:'已同意',
                },{
                    id:'3',
                    name:'李四',
                    sex:'男',
                    age:'24',
                    ac_id:'1',
                    ac_name:'志愿活动1',
                    date:'2020-06-24',
                    status:'已拒绝',
                }],
            };
        },
        methods: {
            isClicked() {
                this.userDialogVisible = true;
            }
        }
    }
</script>
<style>
</style>