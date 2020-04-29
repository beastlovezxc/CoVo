'''
@Author: your name
@Date: 2020-04-25 16:41:21
@LastEditTime: 2020-04-29 23:44:38
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Activity/models.py
'''
from django.db import models

# Create your models here.
# 志愿者活动信息管理 活动编号、活动名称、活动简介、活动是否过期、活动所需人数、参加人数、活动所在地、活动积分、联系人
class Activity(models.Model):
    activity_number = models.AutoField(primary_key=True)    # 活动编号
    activity_name = models.CharField(max_length=20)         # 活动名称
    introduction = models.TextField()                       # 活动简介
    expired = models.BooleanField(default=False)            # 是否过期
    required_num = models.IntegerField(default=0)           # 所需人数
    participants = models.IntegerField(default=0)           # 参加人数
    address = models.CharField(max_length=40)               # 活动所在地
    activity_points = models.IntegerField(default=0)        # 活动积分
    date = models.DateTimeField()                           # 活动时间
    contact = models.CharField(max_length=20)               # 联系人