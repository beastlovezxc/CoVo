'''
@Author: BeanCB
@Date: 2020-05-25 01:02:54
@LastEditors: BeanCB
@LastEditTime: 2020-05-25 01:05:58
@Description: file content
@FilePath: /Covo/Activity/serializers.py
'''
from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_number', 'activity_name', 'introduction', 'expired', 'required_num', 'participants', 'address', 'activity_points', 'date', 'contact')