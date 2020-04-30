'''
@Author: your name
@Date: 2020-04-25 16:53:37
@LastEditTime: 2020-05-01 00:08:49
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
    path('save_walfare/', views.save_walfare, name='save_walfare'),
    path('edit_walfare/<int:prize_number>', views.edit_walfare, name='edit_walfare'),
    path('delete_walfare/<int:prize_number>', views.delete_walfare, name='delete_walfare'),
    # path('walfaremanager/', views.walfaremanager)
    path('walfareinfo/<int:prize_number>', views.get_walfareinfo, name='walfareinfo')
]
