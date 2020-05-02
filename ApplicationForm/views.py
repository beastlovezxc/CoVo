'''
@Author: BeanCB
@Date: 2020-04-25 16:41:36
@LastEditors: BeanCB
@LastEditTime: 2020-05-02 23:45:42
@Description: file content
@FilePath: /Covo/ApplicationForm/views.py
'''
from django.shortcuts import render,HttpResponse

# Create your views here.

def apply(request,activity_number):
    return HttpResponse(activity_number)