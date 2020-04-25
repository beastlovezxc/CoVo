'''
@Author: your name
@Date: 2020-04-25 16:40:41
@LastEditTime: 2020-04-25 17:29:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Manager/views.py
'''
from django.shortcuts import render
from .models import Manager
# Create your views here.
def show_managerlist(request):
    context = {}
    context['managerlist'] = Manager.objects.all()
    return render(request, './Manager/managerlist.html', context)