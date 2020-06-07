<!--
 * @Author: BeanCB
 * @Date: 2020-05-25 23:17:59
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-28 00:01:36
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
            <template slot-scope="scope">
            <el-image
            style="width: 80px; height: 80px"
            :src="scope.row.prize_image"
            :fit="fit">
            </el-image>
            </template>
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="deleteDetail(scope.$index, scope.row)">删除</el-button>
                  <el-button type="text" @click="modifyDetail(scope.$index, scope.row)">修改</el-button>
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
                  <el-input v-model="form.prize_name" placeholder="请输入奖品名称"></el-input>
            </el-form-item>
            <el-form-item label="兑换积分" label-position="left">
                  <el-input v-model="form.prize_points" placeholder="请输入奖品兑换积分"></el-input>
            </el-form-item>
            <el-form-item label="奖品简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="form.prize_introduction" placeholder="请输入奖品简介"></el-input>
            </el-form-item>
            <el-form-item>
                <el-form-item label="福利照片" label-position="left">
                <el-upload
                class="avatar-uploader"
                name="walfareimg"
                action="http://localhost:8000/api/v1/walfare/imgurl/walfare/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess">
                <img v-if="blobUrl" :src="blobUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
                </el-form-item>

            </el-form-item>

        </el-form>
                        <span slot="footer" class="dialog-footer">
                    <el-button @click="dialogVisible = false">取 消</el-button>
                    <el-button 
                    type="primary" 
                    @click="addWalfare">确 认</el-button>
                </span>
        </el-dialog>
        <el-dialog
        title="修改福利奖品"
        :visible.sync="modifyDialogVisible"
        width="30%"
        :before-close="handleClose">
        <el-form>
            <el-form-item label="奖品名称" label-position="left">
                  <el-input v-model="modifyWal.prize_name" placeholder="请输入奖品名称"></el-input>
            </el-form-item>
            <el-form-item label="兑换积分" label-position="left">
                  <el-input v-model="modifyWal.prize_points" placeholder="请输入奖品兑换积分"></el-input>
            </el-form-item>
            <el-form-item label="奖品简介" label-position="left">
                  <el-input 
                  type="textarea" 
                  rows="5"
                  maxlength="500"
                  show-word-limit
                  v-model="modifyWal.prize_introduction" placeholder="请输入奖品简介"></el-input>
            </el-form-item>
            <el-form-item>
                <el-form-item label="福利照片" label-position="left">
                <el-upload
                class="avatar-uploader"
                name="walfareimg"
                action="http://localhost:8000/api/v1/walfare/imgurl/walfare/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess2">
                <img v-if="blobUrl" :src="blobUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
                </el-form-item>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="modifyDialogVisible = false">取 消</el-button>
            <el-button 
            type="primary" 
            @click="modifyConfig">发 布</el-button>
        </span>
        </el-dialog>
    </el-card>
    
</template>
<script>
    export default {
        data() {
            return {
                url: '',
                walUrl:'http://localhost:8000/api/v1/walfare/',
                dialogVisible: false,
                modifyDialogVisible: false,
                imageUrl: '',
                blobUrl: '',
                form: {
                    prize_number: "",
                    prize_name: "",
                    prize_points: "",
                    prize_introduction: "",
                    prize_image: "",
                },
                walfare:[],
                modifyWal: {
                    prize_number: "",
                    prize_name: "",
                    prize_points: "",
                    prize_introduction: "",
                    prize_image: "",
                },
            };
        },
        mounted() {
            this.axios.get(this.walUrl).then((res)=>{
                this.walfare = res.data;
                for(var i = 0; i < this.walfare.length; ++i){
                    var str = this.walfare[i].prize_image
                    this.walfare[i].prize_image = '/img/walfare/'+str;
                }
            })
        },
        methods: {
            handleAvatarSuccess(res, file) {
                this.imageUrl = res.img_path;
                this.blobUrl = '/img/walfare/'+ res.img_path;
            },
            handleAvatarSuccess2(res, file) {
                this.modifyWal.prize_image = res.img_path;
                // this.imageUrl = res.img_path;
                this.blobUrl = '/img/walfare/' + res.img_path;
            },
            deleteDetail(index, rows) {
                this.axios.delete(this.walUrl+rows.prize_number).then((res)=>{
                    alert("删除成功！");
                    this.walfare.splice(index, 1);
                })
                
            },
            modifyDetail(index, rows) {
                this.modifyWal.prize_number = rows.prize_number;
                this.modifyWal.prize_name = rows.prize_name;
                this.modifyWal.prize_points = rows.prize_points;
                this.modifyWal.prize_introduction = rows.prize_points;
                this.modifyWal.prize_image = rows.prize_image.substring(rows.prize_image.lastIndexOf('/')+1);
                this.blobUrl = rows.prize_image;
                this.modifyDialogVisible = true;
                
            },
            addWalfare(){
                this.form.prize_image = this.imageUrl;
                this.axios.post(this.walUrl, this.form).then((res)=>{
                    this.dialogVisible = false;
                })
            },
            modifyConfig(){
                this.axios.put(this.walUrl+this.modifyWal.prize_number, this.modifyWal).then((res)=>{
                    alert('修改成功！');
                    this.modifyDialogVisible = false;
                })
            }
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