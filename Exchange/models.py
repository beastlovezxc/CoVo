'''
@Author: BeanCB
@Date: 2020-04-25 16:42:35
@LastEditors: BeanCB
@LastEditTime: 2020-04-25 21:15:08
@Description: file content
@FilePath: /Covo/Exchange/models.py
'''
from django.db import models

# Create your models here.
#志愿者福利兑换管理 兑换编码（主码）、志愿者编码、礼品编码、兑换时间、成功兑换
class Exchange(models.Model):
    exchange_number = models.AutoField(primary_key=True)    # 兑换编码
    volunteer_number = models.IntegerField(default=0)       # 志愿者编码
    prize_number = models.IntegerField(default=True)        # 礼品编码
    exchange_time = models.DateField()                      # 兑换时间
    exchanged = models.BooleanField(default=True)           # 成功兑换