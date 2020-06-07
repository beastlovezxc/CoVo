<template>
    <el-card>
        <el-table
            :data="exchange_list"
            style="width: 100%"
            :row-class-name="isChoose">
            <el-table-column
            prop="prize_name.prize_number"
            label="奖品编号">
            </el-table-column>
            <el-table-column
            prop="prize_name.prize_name"
            label="奖品名称">
            </el-table-column>
            <el-table-column
            prop="prize_name.prize_introduction"
            label="奖品简介">
            </el-table-column>
            <el-table-column
            prop="prize_name.prize_points"
            label="兑换积分">
            </el-table-column>
            <el-table-column
            prop="prize_name.prize_image"
            label="奖品图片">
            <template slot-scope="scope">
            <el-image
            style="width: 80px; height: 80px"
            :src="scope.row.prize_name.prize_image"
            :fit="fit">
            </el-image>
            <el-table-column
            prop="exchange_time"
            label="兑换日期">
            </el-table-column>
            </template>
            </el-table-column>
        </el-table>
    </el-card>
</template>
<script>
    export default {
        data() {
            return{
                root:'',
                exUrl:'http://localhost:8000/api/v1/exchange/',
                exchange_list:[],
            }
        },
        mounted() {
            this.root = sessionStorage.getItem("account")
            this.axios.get(this.exUrl + this.root).then((res)=> {
                this.exchange_list = res.data;
                for(var i = 0; i < this.exchange_list.length; ++i) {
                    var str = this.exchange_list[i].prize_name.prize_image
                    this.exchange_list[i].prize_name.prize_image = '/img/walfare/' + str;
                    this.exchange_list[i].exchange_time = this.exchange_list[i].exchange_time.substr(0, this.exchange_list[i].exchange_time.indexOf('.')).replace('T', ' ');
                }
            })
        }
    }
</script>