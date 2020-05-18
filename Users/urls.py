'''
@Author: your name
@Date: 2020-04-25 16:45:53
@LastEditTime: 2020-05-18 00:13:58
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Users/urls.py
'''
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('userlist', views.UsersViewSet)
app_name='Users'
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('to_regist/', views.to_regist, name='to_regist'),
    path('regist/', views.regist, name='regist'),
    path('logout/', views.logout, name='logout'),
    path('userlist/', views.show_userlist)
]
