'''
@Author: BeanCB
@Date: 2020-04-25 16:40:36
@LastEditors: BeanCB
@LastEditTime: 2020-05-04 23:23:15
@Description: file content
@FilePath: /Covo/Users/models.py
'''
from django.db import models

# Create your models here.

class Users(models.Model):
    account = models.CharField(primary_key=True,max_length=20)   # 用户名
    password = models.CharField(max_length=20)  # 密码
    manager = models.BooleanField()             # 管理权限

    def __str__(self):
        return self.account