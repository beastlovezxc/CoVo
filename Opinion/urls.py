'''
@Author: your name
@Date: 2020-04-25 16:51:56
@LastEditTime: 2020-04-25 20:35:34
@LastEditors: FengSiJia
@Description: In User Settings Edit
@FilePath: /Covo/Opinion/urls.py
'''
from django.urls import path
from . import views

app_name='Opinion'
urlpatterns = [
    path('opinionlist/', views.get_opinionlist),
    path('opinionInfo/<int:id>', views.get_opinioninfo, name='opinioninfo')
]
