'''
@Author: your name
@Date: 2020-04-25 16:40:41
@LastEditTime: 2020-04-25 17:27:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Manager/models.py
'''
from django.db import models

# Create your models here.
class Manager(models.Model):
    account = models.CharField(max_length=20)   # 用户名-> 外键 User->account
    tel = models.CharField(max_length=20)       # 电话
    index = models.AutoField(primary_key=True)  # 编号
    password = models.CharField(max_length=20)  # 密码