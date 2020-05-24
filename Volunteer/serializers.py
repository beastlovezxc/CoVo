'''
@Author: BeanCB
@Date: 2020-05-24 22:36:43
@LastEditors: BeanCB
@LastEditTime: 2020-05-24 23:37:02
@Description: file content
@FilePath: /Covo/Volunteer/serializers.py
'''
from rest_framework import serializers
from .models import Volunteer
class VolunteerSerializer(serializers.ModelSerializer):
    users_account = serializers.CharField(source="users.account")
    class Meta:
        model = Volunteer
        fields = ('volunteer_number', 'volunteer_name', 'sex', 'age', 'tel', 'address', 'cultural_level', 'activity_points','available_points' , 'users_account')