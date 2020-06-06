from django.db import models
from Users.models import Users
from Activity.models import Activity
from Volunteer.models import Volunteer
# Create your models here.

# 每个志愿者都可以报名一个活动
# 一个活动对应多个报名者
# 管理员可以查看所有报名的结果 （人-活动）
# 也可以查看每个活动所对应报名的人（活动-人）
# 管理员可以接受或者拒绝某个报名人员
# 管理员可以删除某次报名
# 用户可以取消某次报名
# 接受或取消则活动参与人数响应增加或减少
# 若活动需求人数已达上限，则不允许接受

class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    account = models.ForeignKey('Users.Users', on_delete=models.CASCADE)  # 用户名
    activity_number = models.ForeignKey('Activity.Activity', on_delete=models.CASCADE)    # 参与活动序号
    voinfo = models.ForeignKey('Volunteer.Volunteer', on_delete=models.CASCADE)
    status = models.IntegerField(default=0)    # 是否报名成功

    @property
    def users_name(self):
        a_dict = {'user': self.account.account,
                  'password': self.account.password,
                  'manager': self.account.manager}
        return a_dict
    @property
    def activity_name(self):
        a_dict = {  'activity_number':self.activity_number.activity_number,
                    'activity_name':self.activity_number.activity_name,
                    'introduction':self.activity_number.introduction,
                    'expired':self.activity_number.expired,
                    'required_num':self.activity_number.required_num,
                    'participants':self.activity_number.participants,
                    'address':self.activity_number.address,
                    'activity_points':self.activity_number.activity_points,
                    'date':self.activity_number.date,
                    'contact':self.activity_number.contact}
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