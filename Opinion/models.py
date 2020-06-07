'''
@Author: FengSiJia
@Date: 2020-04-25 16:42:07
@LastEditors: FengSiJia
@LastEditTime: 2020-04-25 20:39:13
@Description: file content
'''
from django.db import models

# Create your models here.
#受助人意见管理 求助者编号、活动编号（主码）、求助者姓名、活动名称、反馈时间、反馈内容
class Opinion(models.Model): 
    helper_number = models.IntegerField(default=0)          # 求助者编号
    activity_number = models.IntegerField(default=0)        # 活动编号
    helper_name = models.CharField(max_length=20)           # 求助者姓名
    activity_name = models.CharField(max_length=20)         # 活动名称
    feedback = models.TextField()                           # 反馈内容
    feedback_time = models.DateField()                      # 反馈时间