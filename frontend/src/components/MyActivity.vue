<!--
 * @Author: BeanCB
 * @Date: 2020-05-22 00:13:55
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-29 01:00:43
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/MyActivity.vue
--> 
<template>
    <el-card>
          <el-table
            :data="activity_info"
            style="width: 100%"
            :row-class-name="isExpired"
            @row-click="isClicked"> <!--过期-->
            <el-table-column
            prop="activity_name.activity_number"
            label="活动编号"
            width="180">
            </el-table-column>
            <el-table-column
            prop="activity_name.activity_name"
            label="活动名称"
            width="180">
            </el-table-column>
            <el-table-column
            prop="activity_name.required_num"
            label="活动所需人数">
            </el-table-column>
            <el-table-column
            prop="activity_name.participants"
            label="参加人数">
            </el-table-column>
            <el-table-column
            prop="activity_name.expired"
            label="是否过期">
            <template slot-scope="scope">
              <span v-if="scope.row.activity_name.expired" style="color:red">已过期</span>
              <span v-else >未过期</span>
            </template>
            </el-table-column>
            <el-table-column
            prop="activity_name.activity_points"
            label="活动积分">
            </el-table-column>
            <el-table-column
            prop="activity_name.date"
            label="活动时间">
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click.stop="feedback(scope.row)">发布反馈</el-button>
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
                  <el-input v-model="ac.title" disabled="true" ></el-input>
            </el-form-item>
            <el-form-item label="活动简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="ac.text" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="求助时间" label-position="left">
                <el-input v-model="ac.time" disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="活动所需人数" label-position="left">
                <el-input v-model="ac.people" disabled="true"></el-input>
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
        title="发布反馈"
        :visible.sync="fbDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="反馈内容" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="10"
                  maxlength="500"
                  show-word-limit
                  v-model="fb.feedback" ></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="fbCancel">取 消</el-button>
            <el-button 
            type="primary" 
            @click="fbConfig">确 定</el-button>
        </span>
        </el-dialog>
    </el-card>
</template>
<script>
    export default {
        data() {
            return{
                fbDialogVisible: false,
                acDialogVisible: false,
                root:'',
                applyurl:'http://localhost:8000/api/v1/applicationform/',
                feedbackurl:'http://localhost:8000/api/v1/feedback/',
                fb: {
                  account:'',
                  activity_number:'',
                  feedback:'',
                },
                ac: {
                    title:'志愿活动1',
                    text: '这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111这是志愿活动111',
                    time: '2020-06-25',
                    people: '500',
                },
                activity_info: []
            };
        },
        mounted() {
            this.root = sessionStorage.getItem("account");
            this.axios.get(this.applyurl + this.root).then((res)=>{
            this.activity_info = res.data;
            })
        },
        methods: {
            isExpired({row, rowIndex}) {
                if (row.expired === '是') {
                return 'warning-row';
                }
                // } else if (rowIndex === 3) {
                // return 'success-row';
                // }
                return '';
            },
            isClicked(row)  {
                this.ac.title = row.activity_name.activity_name;
                this.ac.text = row.activity_name.introduction;
                this.ac.time = row.activity_name.date;
                this.ac.people = row.activity_name.required_num;
                this.acDialogVisible = true;
            },
            acCancel() {
                this.acDialogVisible = false;
            },
            acConfig() {
              this.acDialogVisible = false;
            },
            feedback(row) {
              this.fb.account = this.root;
              this.fb.activity_number = row.activity_name.activity_number;
              this.fbDialogVisible = true;
            },
            fbCancel() {
              this.fbDialogVisible = false;
            },
            fbConfig(){
              var _this = this;
              this.axios.post(this.feedbackurl, this.fb).then((res)=>{
                alert('发布成功！');
              });
              this.fbDialogVisible = false;
            },
        }
    }
</script>

<style>
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
</style>