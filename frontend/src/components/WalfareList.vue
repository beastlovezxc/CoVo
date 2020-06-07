<!--
 * @Author: FengSiJia
 * @Date: 2020-05-25 23:52:23
 * @LastEditors: FengSiJia
 * @LastEditTime: 2020-05-25 23:56:49
 * @Description: file content
 * @FilePath: /Covo/frontend/src/components/WalfareList.vue
--> 
<template>
    <el-card>
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
        　　　　　　<el-button type="text" @click.stop="exchangeWalfare(scope.row)">兑换</el-button>
        　　　　</template>
　      　   </el-table-column>  
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return {
                walUrl:'http://localhost:8000/api/v1/walfare/',
                voInfoUrl: 'http://localhost:8000/api/v1/volunteer/',
                dialogVisible: false,
                imageUrl: '',
                root: '',
                available_points: 0,
                form: {
                    name:'',
                    password:'',
                    points: '',
                },
                walfare:[]
            };
        },
        mounted(){
            this.root = sessionStorage.getItem("account");
            this.available_points = sessionStorage.getItem("available_points");
            this.axios.get(this.walUrl).then((res)=>{
                this.walfare = res.data;
                for(var i = 0; i < this.walfare.length; i++) {
                    this.walfare[i].prize_image = '/img/walfare/' + this.walfare[i].prize_image;
                }
            })
        },
        methods:{
            exchangeWalfare(row) {
            if(this.available_points < row.prize_points) {
                alert("剩余积分不足！");
            } else {
                this.available_points -= row.prize_points;
                sessionStorage.setItem("available_points", this.available_points);
                this.axios.put(this.walUrl+this.root+'/'+row.prize_number).then((res)=>{
                    alert("兑换成功！");
                })
            }
        }
        }
        
    }
</script>