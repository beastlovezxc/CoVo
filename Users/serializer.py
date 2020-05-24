'''
@Author: BeanCB
@Date: 2020-05-17 23:50:48
@LastEditors: BeanCB
@LastEditTime: 2020-05-24 22:46:03
@Description: file content
@FilePath: /Covo/Users/serializer.py
'''
from rest_framework import serializers

from Users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('account', 'password', 'manager')