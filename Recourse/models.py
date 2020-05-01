'''
@Author: BeanCB
@Date: 2020-04-25 16:41:48
@LastEditors: BeanCB
@LastEditTime: 2020-05-02 00:03:54
@Description: file content
@FilePath: /Covo/Recourse/models.py
'''
from django.db import models

# Create your models here.
# 求助事件
class Recourse(models.Model):
    index = models.AutoField(primary_key=True)      # 求助编号
    title = models.CharField(max_length=20)         # 求助标题
    text = models.TextField()                       # 求助内容
    time = models.DateTimeField(auto_now_add=True)  # 求助时间
    users = models.ForeignKey('Users.Users', on_delete=models.CASCADE)              # 用户名