'''
@Author: your name
@Date: 2020-04-25 16:45:53
@LastEditTime: 2020-04-25 17:10:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Users/urls.py
'''
from django.urls import path
from . import views
urlpatterns = [
    path('userlist/', views.show_userlist)
]
