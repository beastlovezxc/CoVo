'''
@Author: your name
@Date: 2020-04-25 16:53:37
@LastEditTime: 2020-04-30 23:43:25
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Walfare/urls.py
'''
from django.urls import path
from .import views

app_name='Walfare'
urlpatterns = [
    path('walfarelist/', views.get_walfarelist, name='walfarelist'),
    path('to_walfaremanager/', views.to_walfaremanager, name='to_walfaremanager'),
    path('add_walfare/', views.add_walfare, name='add_walfare'),
    # path('walfaremanager/', views.walfaremanager)
    path('walfareinfo/<int:prize_number>', views.get_walfareinfo, name='walfareinfo')
]
