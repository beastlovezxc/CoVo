'''
@Author: your name
@Date: 2020-04-25 16:53:37
@LastEditTime: 2020-05-12 02:20:53
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Walfare/urls.py
'''
from django.urls import path
from .import views
from django.views.static import serve

app_name='Walfare'
urlpatterns = [
    path('imgurl/walfare/', views.imgUpload),
    path('', views.Walfare_List),
    path('<int:prize_number>', views.Walfare_Detail),
    path('<str:account>/<int:prize_number>', views.exchange_walfare),
    path('walfarelist/', views.get_walfarelist, name='walfarelist'),
    path('to_walfaremanager/', views.to_walfaremanager, name='to_walfaremanager'),
    path('add_walfare/', views.add_walfare, name='add_walfare'),
    path('save_walfare/', views.save_walfare, name='save_walfare'),
    path('edit_walfare/<int:prize_number>', views.edit_walfare, name='edit_walfare'),
    path('delete_walfare/<int:prize_number>', views.delete_walfare, name='delete_walfare'),
    path('exchange/<int:prize_number>', views.exchange, name='exchange'),
    # path('walfaremanager/', views.walfaremanager)
    path('walfareinfo/<int:prize_number>', views.get_walfareinfo, name='walfareinfo')
]
