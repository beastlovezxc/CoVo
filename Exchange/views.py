'''
@Author: BeanCB
@Date: 2020-04-25 16:42:35
@LastEditors: BeanCB
@LastEditTime: 2020-04-25 21:47:32
@Description: file content
@FilePath: /Covo/Exchange/views.py
'''
from django.shortcuts import render
from .models import Exchange
# Create your views here.
def get_exchangelist(request):
    context = {}
    context['exchangelist'] = Exchange.objects.all()
    return render(request, './Exchange/exchange.html', context)