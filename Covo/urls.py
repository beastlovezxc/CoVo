'''
@Author: your name
@Date: 2020-04-25 16:22:23
@LastEditTime: 2020-05-18 00:07:04
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Covo/urls.py
'''
"""Covo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views

app_name = 'Covo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/users/', include('Users.urls')),
    # path('index/', views.showIndex, name='index'),
    # path('users/', include('Users.urls')),
    # path('volunteer/', include('Volunteer.urls')),
    # path('walfare/', include('Walfare.urls')),
    # path('activity/', include('Activity.urls')),
    # path('applicationform/', include('ApplicationForm.urls')),
    # path('exchange/', include('Exchange.urls')),
    # path('recourse/', include('Recourse.urls')),
    # path('manager/', include('Manager.urls')),
    # path('opinion/', include('Opinion.urls')),
    # path('recruit/', include('Recruit.urls')),
]
