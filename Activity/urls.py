'''
@Author: your name
@Date: 2020-04-25 16:49:54
@LastEditTime: 2020-04-25 18:48:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Activity/urls.py
'''
from django.urls import path
from . import views
app_name='Activity'
urlpatterns = [
    path('activitylist/', views.show_activitylist),
    path('activityinfo/<int:activity_number>', views.show_activityinfo, name='activityinfo')
]
