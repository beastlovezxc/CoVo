'''
@Author: your name
@Date: 2020-04-25 16:51:02
@LastEditTime: 2020-04-25 21:17:33
@LastEditors: FengSiJia
@Description: In User Settings Edit
@FilePath: /Covo/Exchange/urls.py
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Exchange_List),
    path('<str:account>', views.Exchange_Detail),
    # path('exchange/', views.get_exchangelist)
]
