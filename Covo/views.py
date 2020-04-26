'''
@Author: BeanCB
@Date: 2020-04-26 21:42:13
@LastEditors: BeanCB
@LastEditTime: 2020-04-26 21:50:36
@Description: file content
@FilePath: /Covo/Covo/views.py
'''

from django.shortcuts import render

def showIndex(request):
    return render(request, './Covo/index.html')