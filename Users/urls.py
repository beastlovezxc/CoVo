'''
@Author: your name
@Date: 2020-04-25 16:45:53
@LastEditTime: 2020-04-26 22:19:01
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Users/urls.py
'''
from django.urls import path
from . import views
app_name='Users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('userlist/', views.show_userlist)
]
