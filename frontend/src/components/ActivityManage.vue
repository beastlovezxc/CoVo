<!--
 * @Author: BeanCB
 * @Date: 2020-05-26 00:02:27
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 02:10:09
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/ActivityManage.vue
--> 
<template>
    <el-card>
        <div id="recourse-header-title">求助活动列表<el-button type="primary" @click="pubDialogVisible = true">发布求助活动</el-button></div>
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
            label="是否过期">
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
        　　　　　　<el-button type="text" @click.stop="checkDetail(scope.$index, activity_list)">删除</el-button>
                  <el-button type="text" @click.native.stop="checkDetail(scope.row.phone)">修改</el-button>
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
                  <el-input v-model="pub.title" placeholder="请输入活动名称"></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  placeholder="请输入活动介绍"
                  v-model="pub.text"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="pub.time" placeholder="请输入活动时间"></el-input>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="pub.people" placeholder="请填写活动所需人数"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="pubCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="pubConfig">确 定</el-button>
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
                pub: {
                    title: '',
                    text: '',
                    time: '',
                    people: '',
                },
                ac: {
                    title: '求助标题1',
                    text: '求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1求助内容1',
                    time: '2020-06-05',
                    people: '50',
                },
                activity_list: [{
                    activity_number: '1',
                    activity_name: '志愿活动1',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '2020.04.02',
                    ops: '450',
                    }, {
                    activity_number: '2',
                    activity_name: '志愿活动2',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '500',
                    ops: '450',
                    }, {
                    activity_number: '3',
                    activity_name: '志愿活动3',
                    required_num: '500',
                    participants: '450',
                    expired: '否',
                    activity_points: "150",
                    date: '500',
                    ops: '450',
                    }, {
                    activity_number: '4',
                    activity_name: '志愿活动4',
                    required_num: '500',
                    participants: '450',
                    expired: '是',
                    activity_points: "150",
                    date: '500',
                    ops: '参加',
                    }]
            };
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
                this.acDialogVisible = true;
            },
            acCancel() {
                this.acDialogVisible = false;
            },
            acConfig() {
                this.acDialogVisible = false;
            },
            pubConfig() {
                this.pubDialogVisible = false;
            },
            pubCancel() {
                this.pubDialogVisible = false;
            },
            checkDetail(index, rows) {
                rows.splice(index, 1);
            },
        }
    }
</script>