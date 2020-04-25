'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-04-25 21:07:38
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

def get_walfareinfo(request, prize_number):
    context = {}
    context['walfareinfo'] = Walfare.objects.get(prize_number=prize_number)
    return render(request, './Walfare/walfareinfo.html', context)