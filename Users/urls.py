# '''
# @Author: your name
# @Date: 2020-04-25 16:45:53
# @LastEditTime: 2020-06-02 23:27:03
# @LastEditors: BeanCB
# @Description: In User Settings Edit
# @FilePath: \Covo\Users\urls.py
# '''
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url

# router = DefaultRouter()
# router.register('userlist', views.UsersViewSet)
app_name='Users'
urlpatterns = [
    path('', views.User_List),
    path('<str:account>', views.User_Detail),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('to_regist/', views.to_regist, name='to_regist'),
    path('regist/', views.regist, name='regist'),
    path('logout/', views.logout, name='logout'),
    path('userlist/', views.show_userlist),
    url(r'^api/v1/auth/$', views.AuthView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)