<!--
 * @Author: BeanCB
 * @Date: 2020-05-25 23:17:59
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-25 23:51:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/WalfaraManage.vue
--> 
<template>
    <el-card>
        <div id="walfara-header-title">福利兑换管理<el-button type="primary" @click="dialogVisible = true">增加</el-button></div>
        <el-table
            :data="walfare"
            style="width: 100%"
            :row-class-name="isChoose">
            <el-table-column
            prop="prize_number"
            label="奖品编号">
            </el-table-column>
            <el-table-column
            prop="prize_name"
            label="奖品名称">
            </el-table-column>
            <el-table-column
            prop="prize_introduction"
            label="奖品简介">
            </el-table-column>
            <el-table-column
            prop="prize_points"
            label="兑换积分">
            </el-table-column>
            <el-table-column
            prop="prize_image"
            label="奖品图片">
            <el-image
            style="width: 80px; height: 80px"
            :src="url"
            :fit="fit">
            </el-image>
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">删除</el-button>
                  <el-button type="text" @click="checkDetail(scope.row.phone)">修改</el-button>
        　　　　</template>
　      　   </el-table-column>  
        </el-table>
        <el-dialog
        title="增加福利奖品"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="奖品名称" label-position="left">
                  <el-input v-model="form.name" placeholder="请输入奖品名称"></el-input>
            </el-form-item>
            <el-form-item label="兑换积分" label-position="left">
                  <el-input v-model="form.points" placeholder="请输入奖品兑换积分"></el-input>
            </el-form-item>
            <el-form-item label="奖品简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="form.name" placeholder="请输入奖品简介"></el-input>
            </el-form-item>
            <el-form-item>
                <el-form-item label="福利照片" label-position="left">
                <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
                </el-form-item>
            </el-form-item>

        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="dialogVisible = false">发 布</el-button>
        </span>
        </el-dialog>
    </el-card>
    
</template>
<script>
    export default {
        data() {
            return {
                url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                dialogVisible: false,
                imageUrl: '',
                form: {
                    name:'',
                    password:'',
                    points: '',
                },
                walfare:[{
                    prize_number: "1",
                    prize_name: "足球",
                    prize_points: "550",
                    prize_introduction: "有温度的奖品",
                    prize_image: "url",
                }]
            };
        },
        methods: {
            handleAvatarSuccess(res, file) {
                this.imageUrl = URL.createObjectURL(file.raw);
            },
        }
    }
</script>
<style>
#walfara-header-title {
    display: flex;
    text-align: left;
    justify-content: space-between;
    font-size: 2em;
}

  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 40px;
    height: 40px;
    line-height: 40px;
    text-align: center;
  }
  .avatar {
    width: 40px;
    height: 40px;
    display: block;
  }
</style>