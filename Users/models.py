'''
@Author: FengSiJia
@Date: 2020-04-25 16:40:36
@LastEditors: FengSiJia
@LastEditTime: 2020-05-24 20:03:12
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

class userToken(models.Model):
  username = models.OneToOneField(to='Users',on_delete=models.DO_NOTHING)
  token = models.CharField(max_length=60)