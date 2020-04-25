'''
@Author: your name
@Date: 2020-04-25 16:41:21
@LastEditTime: 2020-04-25 18:50:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Activity/views.py
'''
from django.shortcuts import render
from .models import Activity
# Create your views here.
def show_activitylist(request):
    context = {}
    
    context['activitylist'] = Activity.objects.all().values('activity_number', 'activity_name')
    return render(request, './Activity/activitylist.html', context)

def show_activityinfo(request, activity_number):
    context = {}
    context['activityinfo'] = Activity.objects.get(activity_number=activity_number)
    return render(request, './Activity/activityinfo.html', context)