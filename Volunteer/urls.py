'''
@Author: your name
@Date: 2020-04-25 16:53:12
@LastEditTime: 2020-04-28 00:18:20
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Volunteer/urls.py
'''
from django.urls import path
from . import views
app_name='Volunteer'
urlpatterns = [
    path('setInfo/',views.setInfo, name='setInfo'),
    path('to_setInfo/', views.to_setInfo, name='to_setInfo'),
    path('volunteerlist/', views.get_volunteerlist),
    path('volunteerinfo/<int:volunteer_number>', views.get_volunteerinfo, name='volunteerinfo')
]
