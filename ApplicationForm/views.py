'''
@Author: BeanCB
@Date: 2020-04-25 16:41:36
@LastEditors: BeanCB
@LastEditTime: 2020-05-03 00:56:24
@Description: file content
@FilePath: /Covo/ApplicationForm/views.py
'''
from django.shortcuts import render,HttpResponse
from .models import Apply
from Users.models import Users
from Activity.models import Activity
# Create your views here.

def apply(request,activity_number):
    account = request.session['account']
    user = Users.objects.get(account=account)
    activity = Activity.objects.get(activity_number=activity_number)
    if activity.required_num == activity.participants:
        return HttpResponse('人数已满')
    ap = Apply.objects.all().filter(account=user, activity_number=activity)
    if not ap:
        ap = Apply.objects.create(account=user, activity_number=activity)
        ap.save()
        return HttpResponse('已成功报名')
    return HttpResponse('您已经报过名了')