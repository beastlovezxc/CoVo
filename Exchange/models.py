'''
@Author: FengSiJia
@Date: 2020-04-25 16:42:35
@LastEditors: FengSiJia
@LastEditTime: 2020-04-25 21:15:08
@Description: file content
@FilePath: /Covo/Exchange/models.py
'''
from django.db import models
from Users.models import Users
from Walfare.models import Walfare
from Volunteer.models import Volunteer
# Create your models here.
#志愿者福利兑换管理 兑换编码（主码）、志愿者编码、礼品编码、兑换时间、成功兑换
class Exchange(models.Model):
    exchange_number = models.AutoField(primary_key=True)    # 兑换编码
    exchange_time = models.DateTimeField(auto_now_add=True)                      # 兑换时间
    account = models.ForeignKey('Users.Users', on_delete=models.CASCADE)  # 用户名    # 参与活动序号
    voinfo = models.ForeignKey('Volunteer.Volunteer', on_delete=models.CASCADE)
    prize_info = models.ForeignKey('Walfare.Walfare', on_delete=models.CASCADE)
    exchanged = models.BooleanField(default=True)           # 成功兑换

    @property
    def prize_name(self):
        a_dict = {
            'prize_number': self.prize_info.prize_number,
            'prize_name': self.prize_info.prize_name,
            'prize_points': self.prize_info.prize_points,
            'prize_introduction': self.prize_info.prize_introduction,
            'prize_image': self.prize_info.prize_image
        }
        return a_dict
    @property
    def users_name(self):
        a_dict = {
            'user': self.account.account,
            'password': self.account.password,
            'manager': self.account.manager
        }
        return a_dict

    @property
    def voinfo_name(self):
        a_dict = {
            'volunteer_number': self.voinfo.volunteer_number,
            'volunteer_name': self.voinfo.volunteer_name,
            'sex': self.voinfo.sex,
            'age': self.voinfo.age,
            'tel': self.voinfo.tel,
            'address': self.voinfo.address,
            'cultural_level': self.voinfo.cultural_level,
            'activity_points': self.voinfo.activity_points,
            'available_points': self.voinfo.available_points,
        }
        return a_dict