'''
@Author: your name
@Date: 2020-04-25 16:51:24
@LastEditTime: 2020-04-28 23:35:53
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Recourse/urls.py
'''
from django.urls import path
from . import views

app_name='Recourse'
urlpatterns = [
    path('to_recourse/', views.to_recourse, name='to_recourse'),
    path('record_recourse/', views.record_recourse, name='record_recourse'),
    # path('helperlist/', views.get_helperlist),
    # path('helperinfo/<int:helper_number>', views.get_helperinfo, name='helperinfo'),
]