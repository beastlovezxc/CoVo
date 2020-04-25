'''
@Author: your name
@Date: 2020-04-25 16:40:36
@LastEditTime: 2020-04-25 17:19:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Users/views.py
'''
from django.shortcuts import render
from .models import Users
# Create your views here.
def show_userlist(request):
    context = {}
    context['userlist'] = Users.objects.all()
    return render(request, './Users/userlist.html', context)