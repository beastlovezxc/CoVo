'''
@Author: FengSiJia
@Date: 2020-04-25 16:41:48
@LastEditors: FengSiJia
@LastEditTime: 2020-06-06 02:15:17
@Description: file content
@FilePath: \Covo\Recourse\models.py
'''
from django.db import models

# Create your models here.
# 求助事件
class Recourse(models.Model):
    index = models.AutoField(primary_key=True)      # 求助编号
    title = models.CharField(max_length=20)         # 求助标题
    text = models.TextField()                       # 求助内容
    time = models.DateTimeField(auto_now_add=True)  # 求助时间
    status = models.IntegerField(default=0)         # 求助状态   0: 求助中  1: 已完成  2: 已拒绝
    activity_num = models.IntegerField(default=-1)  # 活动编号
    users = models.ForeignKey('Users.Users', on_delete=models.CASCADE)              # 用户名