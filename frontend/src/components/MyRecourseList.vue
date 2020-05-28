<!--
 * @Author: BeanCB
 * @Date: 2020-05-26 00:12:28
 * @LastEditors: BeanCB
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
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100" prop="status">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button  type="text" @click.stop="checkDetail(scope.row.phone)">撤 销</el-button>
                  <el-button  type="text" @click.stop="checkModify(scope.row.phone)">修 改</el-button>
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

        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
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
                pushDialogVisible: false,
                form: {
                    name:'',
                    password:'',
                },
                re: {
                    title: '求助活动1',
                    text: '这是求助活动1这是求助活动1这是求助活动1这是求助活动1这是求助活动1这是求助活动1',
                },
                recourse_list: [{
                    index:'1',
                    title:'求助活动1',
                    time:'2020-06-20',
                    status:'求助中',
                },{
                    index:'2',
                    title:'求助活动2',
                    time:'2020-06-25',
                    status:'求助中',
                },
                {
                    index:'3',
                    title:'求助活动3',
                    time:'2020-06-27',
                    status:'求助中',
                }],
            };
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
                    this.pushDialogVisible = true;
                },
                checkModify(index, rows) {
                    this.dialogVisible = true;
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