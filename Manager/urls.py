'''
@Author: your name
@Date: 2020-04-25 16:51:41
@LastEditTime: 2020-04-25 17:25:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Manager/urls.py
'''
from django.urls import path
from . import views
urlpatterns = [
    path('managerlist/', views.show_managerlist)
]
