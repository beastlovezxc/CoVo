'''
@Author: your name
@Date: 2020-04-25 16:50:41
@LastEditTime: 2020-05-02 23:46:09
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/ApplicationForm/urls.py
'''
from django.urls import path
from . import views

app_name='ApplicationForm'
urlpatterns = [
    path('apply/<int:activity_number>', views.apply, name='apply'),
]
