'''
@Author: your name
@Date: 2020-04-25 16:51:24
@LastEditTime: 2020-04-25 20:14:41
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Helper/urls.py
'''
from django.urls import path
from . import views

app_name='Helper'
urlpatterns = [
    path('helperlist/', views.get_helperlist),
    path('helperinfo/<int:helper_number>', views.get_helperinfo, name='helperinfo'),
]
