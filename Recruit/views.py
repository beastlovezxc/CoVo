'''
@Author: BeanCB
@Date: 2020-04-25 16:40:57
@LastEditors: BeanCB
@LastEditTime: 2020-05-04 23:45:32
@Description: file content
@FilePath: /Covo/Recruit/views.py
'''
from django.shortcuts import render,HttpResponse
from . import models
from ApplicationForm.models import Apply

# Create your views here.
# def to_recruit(request)
def recruitlist(request):
    context = {}
    context['applylist'] = Apply.objects.all()
    print(context['applylist'])
    return render(request, './Recruit/recruitlist.html', context)

def agree(request, apply_id):
    return HttpResponse('Agree')

def refuse(request, apply_id):
    return HttpResponse('Refuse')