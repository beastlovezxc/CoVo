'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-04-25 20:45:06
@Description: file content
@FilePath: /Covo/Walfare/models.py
'''
from django.db import models

# Create your models here.
#志愿者福利管理 奖品编号（主码）、奖品名称、奖品积分、奖品简介、奖品图片
class Walfare(models.Model):
    prize_number = models.AutoField(primary_key=True)       # 奖品编号
    prize_name = models.CharField(max_length=40)            # 奖品名称
    prize_points = models.IntegerField(default=0)           # 奖品积分
    prize_introduction = models.TextField()                 # 奖品简介
    prize_image = models.CharField(max_length=200)          # 奖品图片