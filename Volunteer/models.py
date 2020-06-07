'''
@Author: your name
@Date: 2020-04-25 16:41:09
@LastEditTime: 2020-04-27 23:18:24
@LastEditors: FengSiJia
@Description: In User Settings Edit
@FilePath: /Covo/Volunteer/models.py
'''
from django.db import models

# Create your models here.
# 志愿者信息管理 志愿者编号（主码）、志愿者姓名、性别、年龄、地址、手机号、文化水平、志愿活动积分、可用积分、用户名、登录密码
class Volunteer(models.Model):
    volunteer_number = models.AutoField(primary_key=True)   # 志愿者编号 主键
    volunteer_name = models.CharField(max_length=20)        # 姓名
    sex = models.BooleanField(default=True)                 # 性别
    age = models.IntegerField(null=True)                    # 年龄
    tel = models.CharField(max_length=20)                   # 电话
    address = models.CharField(max_length=40)               # 地址
    cultural_level = models.CharField(max_length=20)        # 文化水平
    activity_points = models.IntegerField(default=0)        # 志愿者活动积分
    available_points = models.IntegerField(default=0)       # 可用积分
    users = models.ForeignKey('Users.Users', on_delete=models.CASCADE, null=True)
    # account = models.CharField(max_length=20)               # 用户名 -> 外键 User->account