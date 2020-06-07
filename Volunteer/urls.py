# '''
# @Author: your name
# @Date: 2020-04-25 16:53:12
# @LastEditTime: 2020-06-04 00:36:22
# @LastEditors: FengSiJia
# @Description: In User Settings Edit
# @FilePath: \Covo\Volunteer\urls.py
# '''
from django.urls import path
from . import views
from django.conf.urls import url

app_name='Volunteer'
urlpatterns = [
    path('', views.Volunteer_List),
    path('<str:account>', views.Volunteer_Detail),
    path('setInfo/',views.setInfo, name='setInfo'),
    path('to_setInfo/', views.to_setInfo, name='to_setInfo'),
    path('volunteerlist/', views.get_volunteerlist, name='volunteerlist'),
    path('volunteerinfo/<str:account>', views.get_volunteerinfo, name='volunteerinfo'),
    url(r'^volunteer/$', views.VolunteerList.as_view()),
    url(r'^volunteer/(?P<pk>[a-zA-Z0-9]{1,})/$', views.VolunteerDetail.as_view()),
]
