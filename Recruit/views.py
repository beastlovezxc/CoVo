'''
@Author: FengSiJia
@Date: 2020-04-25 16:40:57
@LastEditors: FengSiJia
@LastEditTime: 2020-05-24 19:53:59
@Description: file content
@FilePath: /Covo/Recruit/views.py
'''
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from . import models
from ApplicationForm.models import Apply
from Activity.models import Activity

# Create your views here.
# def to_recruit(request)
def recruitlist(request):
    context = {}
    context['applylist'] = Apply.objects.all().values()
    print(context['applylist'])
    aplist = list(context['applylist'])
    return JsonResponse(aplist, safe=False)
    # return render(request, './Recruit/recruitlist.html', context)

def agree(request, apply_id):
    apply = Apply.objects.get(id=apply_id)
    activity = apply.activity_number
    if apply.status is True:
        return HttpResponse('已同意此人报名，勿重复操作！')
    if activity.required_num == activity.participants:
        return HttpResponse('报名人数已满！')
    activity.participants += 1
    activity.save()
    apply.status = True
    apply.save()
    return redirect('/recruit/recruitlist/')

def refuse(request, apply_id):
    apply = Apply.objects.get(id=apply_id)
    activity = apply.activity_number
    if activity.participants == 0:
        return redirect('/recruit/recruitlist/')
    activity.participants -= 1
    activity.save()
    apply.status = False
    apply.save()
    return redirect('/recruit/recruitlist/')