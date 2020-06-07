'''
@Author: FengSiJia
@Date: 2020-06-04 00:25:00
@LastEditors: FengSiJia
@LastEditTime: 2020-06-04 00:34:05
@Description: file content
@FilePath: \Covo\Volunteer\serializer.py
'''
from rest_framework import serializers
from .models import Volunteer

class VolunteerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ('volunteer_number', 'volunteer_name', 'sex', 'age', 'tel', 'address', 'cultural_level', 'activity_points', 'available_points', 'users')