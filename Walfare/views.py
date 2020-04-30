'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-04-30 23:43:56
@Description: file content
@FilePath: /Covo/Walfare/views.py
'''
from django.shortcuts import render
from .models import Walfare
# Create your views here.
def get_walfarelist(request):
    context = {}
    context['walfarelist'] = Walfare.objects.all().values('prize_number','prize_name', 'prize_points')
    return render(request, './Walfare/walfarelist.html', context)

def to_walfaremanager(request):
    return render(request, './Walfare/walfaremanager.html')

def add_walfare(request):
    return render(request, './Walfare/add_walfare.html')

def get_walfareinfo(request, prize_number):
    context = {}
    context['walfareinfo'] = Walfare.objects.get(prize_number=prize_number)
    return render(request, './Walfare/walfareinfo.html', context)