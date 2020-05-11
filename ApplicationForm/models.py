'''
@Author: BeanCB
@Date: 2020-04-25 16:41:36
@LastEditors: BeanCB
@LastEditTime: 2020-05-12 01:45:18
@Description: file content
@FilePath: /Covo/ApplicationForm/models.py
'''
from django.db import models
from Users.models import Users
from Activity.models import Activity
# Create your models here.

# 每个志愿者都可以报名一个活动
# 一个活动对应多个报名者
# 管理员可以查看所有报名的结果 （人-活动）
# 也可以查看每个活动所对应报名的人（活动-人）
# 管理员可以接受或者拒绝某个报名人员
# 管理员可以删除某次报名
# 用户可以取消某次报名
# 接受或取消则活动参与人数响应增加或减少
# 若活动需求人数已达上限，则不允许接受

class Apply(models.Model):
    account = models.ForeignKey('Users.Users', on_delete=models.CASCADE)  # 用户名
    activity_number = models.ForeignKey('Activity.Activity', on_delete=models.CASCADE)    # 参与活动序号
    status = models.BooleanField()    # 是否报名成功

