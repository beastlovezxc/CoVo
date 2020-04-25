'''
@Author: your name
@Date: 2020-04-25 16:53:37
@LastEditTime: 2020-04-25 21:03:59
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Walfare/urls.py
'''
from django.urls import path
from .import views

app_name='Walfare'
urlpatterns = [
    path('walfarelist/', views.get_walfarelist),
    path('walfareinfo/<int:prize_number>', views.get_walfareinfo, name='walfareinfo')
]
