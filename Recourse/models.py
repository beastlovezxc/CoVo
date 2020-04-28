'''
@Author: BeanCB
@Date: 2020-04-25 16:41:48
@LastEditors: BeanCB
@LastEditTime: 2020-04-28 23:54:06
@Description: file content
@FilePath: /Covo/Recourse/models.py
'''
from django.db import models

# Create your models here.
# 求助者信息管理 求助者编号（主码）、求助者姓名、地址、手机号、用户名、登录密码
class Recourse(models.Model):
    index = models.AutoField(primary_key=True)      # 求助编号
    title = models.CharField(max_length=20)         # 求助标题
    text = models.TextField()                       # 求助内容
    time = models.DateTimeField(auto_now_add=True)  # 求助时间
    users = models.ForeignKey('Users.Users', on_delete=models.CASCADE, null=True)              # 用户名