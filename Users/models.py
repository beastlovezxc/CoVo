from django.db import models

# Create your models here.

class Users(models.Model):
    account = models.CharField(primary_key=True,max_length=20)   # 用户名
    password = models.CharField(max_length=20)  # 密码
    manager = models.BooleanField()             # 管理权限