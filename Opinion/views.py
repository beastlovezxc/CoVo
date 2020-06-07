'''
@Author: FengSiJia
@Date: 2020-04-25 16:42:07
@LastEditors: FengSiJia
@LastEditTime: 2020-04-25 20:42:26
@Description: file content
'''
from django.shortcuts import render
from .models import Opinion
# Create your views here.

def get_opinionlist(request):
    context = {}
    context['opinionlist'] = Opinion.objects.all().values('id','helper_name', 'activity_name', 'feedback_time')
    return render(request, './Opinion/opinionlist.html', context)

def get_opinioninfo(request, id):
    context = {}
    context['opinioninfo'] = Opinion.objects.all().get(id=id)
    return render(request, './Opinion/opinioninfo.html', context)