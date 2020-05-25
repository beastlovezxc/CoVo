<!--
 * @Author: BeanCB
 * @Date: 2020-05-25 23:52:23
 * @LastEditors: BeanCB
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
            <el-image
            style="width: 80px; height: 80px"
            :src="url"
            :fit="fit">
            </el-image>
            </el-table-column>
            <el-table-column label="操作" align="center" min-width="100">
        　　　　<template slot-scope="scope">
        　　　　　　<el-button type="text" @click="checkDetail(scope.row.phone)">兑换</el-button>
        　　　　</template>
　      　   </el-table-column>  
        </el-table>
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
        }
    }
</script>