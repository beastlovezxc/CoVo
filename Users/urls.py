'''
@Author: your name
@Date: 2020-04-25 16:45:53
@LastEditTime: 2020-04-27 20:58:19
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Users/urls.py
'''
from django.urls import path
from . import views
app_name='Users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('to_regist/', views.to_regist, name='to_regist'),
    path('regist/', views.regist, name='regist'),
    path('userlist/', views.show_userlist)
]
