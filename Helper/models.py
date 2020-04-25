from django.db import models

# Create your models here.
# 求助者信息管理 求助者编号（主码）、求助者姓名、地址、手机号、用户名、登录密码
class Helper(models.Model):
    helper_number = models.AutoField(primary_key=True)      # 求助者编号
    helper_name = models.CharField(max_length=20)           # 求助者姓名
    helper_tel = models.CharField(max_length=20)            # 手机号
    helper_address = models.CharField(max_length=40)        # 地址
    account = models.CharField(max_length=20)               # 用户名