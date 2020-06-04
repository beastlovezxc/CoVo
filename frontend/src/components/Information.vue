<!--
 * @Author: BeanCB
 * @Date: 2020-05-20 23:46:55
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-06-04 23:38:15
 * @Description: file content
 * @FilePath: \Covo\frontend\src\components\Information.vue
--> 
<template>
    <el-card class="info-card">
        <el-form ref="form" :model="model" label-width="80px">
            <div class="content-title">基本资料</div>
            <div class="info">请完善一下信息，方便报名资料填写</div>
            <div class="content-in">基本信息</div>
            <div class="content-in-in"><span>用户名：</span><span>{{form.users}}</span></div>
            <el-form-item label="姓名:" label-position="left">
                <el-col :span="5">
                  <el-input v-model="form.volunteer_name" placeholder="请输入姓名" :disabled="isDisabled"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item label="性别:" label-position="left">
                <el-select v-model="form.sex" placeholder="请选择性别" :disabled="isDisabled">
                  <el-option label="男" value="1"></el-option>
                  <el-option label="女" value="0"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="年龄:" label-position="left">
                <el-col :span="5">
                  <el-input v-model="form.age" placeholder="请输入年龄" :disabled="isDisabled"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item label="电话:" label-position="left">
                <el-col :span="5">
                  <el-input v-model="form.tel" placeholder="请输入电话" :disabled="isDisabled"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item label="地址:" label-position="left">
                <el-col :span="10">
                  <el-input v-model="form.address" placeholder="请输入地址" :disabled="isDisabled"></el-input>
                </el-col>
            </el-form-item>
            <el-form-item label="文化水平:" label-position="left">
                <el-select v-model="form.cultural_level" placeholder="请选择文化水平" :disabled="isDisabled">
                  <el-option label="小学" value="小学"></el-option>
                  <el-option label="初中" value="初中"></el-option>
                  <el-option label="高中" value="高中"></el-option>
                  <el-option label="专科" value="专科"></el-option>
                  <el-option label="本科" value="本科"></el-option>
                  <el-option label="硕士" value="硕士"></el-option>
                  <el-option label="博士" value="博士"></el-option>
                </el-select>
            </el-form-item>
        </el-form>
        <div class="btn">
          <div class="btn2">
            <el-button 
            type="primary" 
            @click="pubConfig">修改</el-button>
          <el-button 
            type="primary" 
            @click="pubConfirm">确 定</el-button>
            </div>
        </div>
        
    </el-card>
</template>
<script>
export default {
  data() {
    return {
      url: 'http://localhost:8000/api/v1/volunteer/',
      isDisabled: true,
      root: '',
      form: {
          volunteer_number: '',
          volunteer_name: '',
          sex: '',
          age: '',
          tel:'',
          address:'',
          cultural_level:'',
          activity_points:'',
          available_points:'',
          volunteer_number:'',
        },
    };
  },
  mounted() {
          this.root = sessionStorage.getItem("account");
          let url = 'http://localhost:8000/volunteer/volunteer/' + this.root + '/';
          console.log(url);
          this.axios.get(url, {
          }).then((res)=> {
            this.form.users = res.data.users_account;
            this.form.volunteer_name = res.data.volunteer_name;
            this.form.age = res.data.age;
            this.form.address = res.data.address;
            this.form.tel = res.data.tel;
            this.form.cul_level = res.data.cultural_level;
            this.form.activity_points = res.data.activity_points;
            this.form.available_points = res.data.available_points;
            this.form.volunteer_number = res.data.volunteer_number;
            if (res.data.sex) {
                this.form.sex = '男';
            } else {
                this.form.sex = '女';
            }
            
            // alert(res.data.cultural_level);
          });
        },
  methods:{
      pubConfig() {
        this.isDisabled = false;
      },
      pubConfirm() {
        if( this.form.sex === '男') {
          this.form.sex = 1;
        } else {
          this.form.sex = 0;
        }
        this.axios.put(this.url + this.form.users, this.form).then((res)=> {
          alert("success!");
        })
        this.isDisabled = true;

      }
  }
};
</script>
<style>
.el-form-item {
  font-weight: bolder;
}
.info-card {
  text-align: left;
  margin: 0 0 0 0;
}
.info {
  padding-top: 10px;
  padding-bottom: 10px;
  padding: 6px 12px;
  line-height: 18px;
  margin-top:0px;
  margin-bottom: 6px;
  border-radius: 0px;
  color: #555;
  background-color: #F9F9F9;
  border-color: #DDD;
  border: 1px solid transparent;
  margin: 0;
  box-sizing: border-box;
  font-family: "Helvetica Neue", "Luxi Sans", "DejaVu Sans", Tahoma, "Hiragino Sans GB", STHeiti, "Microsoft YaHei";
  font-size: 12px;
}
.content-title {
  border-bottom: 1px solid #DDD;
  padding: 16px 0px;
  /* min-height: 70px; */
  margin: 0;
  box-sizing: border-box;
  font-family: "Helvetica Neue", "Luxi Sans", "DejaVu Sans", Tahoma, "Hiragino Sans GB", STHeiti, "Microsoft YaHei";
  line-height: 1.428571429;
  color: #333333;
}
.content-in {
  font-family: "Helvetica Neue", "Luxi Sans", "DejaVu Sans", Tahoma, "Hiragino Sans GB", STHeiti, "Microsoft YaHei";
  font-size: 14px;
  margin-top: 10px;
  margin-bottom: 10px;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
.content-in-in {
    height: 50px;
    
    font-weight: bolder;
    font-size: 14px;
    color: #666;
    text-indent: 2.5em;
}
.btn {
  width: 200px;
  /* align-content: center; */
  position:relative;
  margin: 0 auto;
}
.btn2 {
  margin: 0 auto;
  /* position: absolute; */
  left: 400px;
}
</style>