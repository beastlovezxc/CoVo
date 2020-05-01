'''
@Author: your name
@Date: 2020-04-25 16:49:54
@LastEditTime: 2020-05-02 00:14:32
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Activity/urls.py
'''
from django.urls import path
from . import views
app_name='Activity'
urlpatterns = [
    path('to_recruit/', views.to_recruit, name='to_recruit'),
    path('recruit/', views.recruit, name='recruit'),
    path('activitylist/', views.activitylist, name='activitylist'),
    path('activityinfo/<int:activity_number>', views.show_activityinfo, name='activityinfo')
]
