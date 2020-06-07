'''
@Author: your name
@Date: 2020-04-25 16:49:54
@LastEditTime: 2020-05-25 01:09:52
@LastEditors: FengSiJia
@Description: In User Settings Edit
@FilePath: /Covo/Activity/urls.py
'''
from django.urls import path
from . import views
from django.conf.urls import url
app_name='Activity'
urlpatterns = [
    path('', views.Activity_List),
    path('<int:activity_number>', views.Activity_Detail),
    path('to_recruit/', views.to_recruit, name='to_recruit'),
    path('recruit/', views.recruit, name='recruit'),
    path('activitylist/', views.activitylist, name='activitylist'),
    path('activityinfo/<int:activity_number>', views.show_activityinfo, name='activityinfo'),
    url(r'^activity/$', views.VolunteerList.as_view()),
    url(r'^activity/(?P<pk>[a-zA-Z0-9]{1,})/$', views.VolunteerDetail.as_view()),
]
