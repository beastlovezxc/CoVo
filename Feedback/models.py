from django.db import models
from Users.models import Users
from Activity.models import Activity
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    account = models.ForeignKey('Users.Users', on_delete=models.CASCADE)  # 用户名
    activity_number = models.ForeignKey('Activity.Activity', on_delete=models.CASCADE)    # 参与活动序号
    feedback = models.TextField()    # 反馈内容
    time = models.DateTimeField(auto_now=True)

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
