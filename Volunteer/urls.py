'''
@Author: your name
@Date: 2020-04-25 16:53:12
@LastEditTime: 2020-04-25 19:23:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Volunteer/urls.py
'''
from django.urls import path
from . import views
app_name='Volunteer'
urlpatterns = [
    path('volunteerlist/', views.get_volunteerlist),
    path('volunteerinfo/<int:volunteer_number>', views.get_volunteerinfo, name='volunteerinfo')
]
