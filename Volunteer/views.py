'''
@Author: your name
@Date: 2020-04-25 16:41:09
@LastEditTime: 2020-05-12 01:23:02
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Volunteer/views.py
'''
from django.shortcuts import render
from .models import Volunteer
from Users.models import Users
# Create your views here.
def get_volunteerlist(request):
    context = {}
    context['volulist'] = Volunteer.objects.all().values('volunteer_number','volunteer_name')
    return render(request, './Volunteer/volunteerlist.html', context)

def get_volunteerinfo(request, account):
    context = {}
    print(account)
    user = Users.objects.get(account=account)
    vo_info = user.volunteer_set.all().get(users=user)
    if vo_info:
        context['volunteerinfo'] = vo_info
        return render(request, './Volunteer/volunteerinfo.html', context)
    else:
        return render(request, './Volunteer/to_setInfo.html')

def to_setInfo(request):
    return render(request, './Volunteer/to_setInfo.html', context)

def setInfo(request):
    context = {}
    vo_info = Volunteer.objects.get(volunteer_number=volunteer_number)
    if vo_info:
        request.session['ac_points'] = vo_info.activity_points
        request.session['av_points'] = vo_info.available_points
        context['ac_points'] = vo_info.activity_points
        context['av_points'] = vo_info.available_points
        context['is_manager'] = False
        return render(request,'./Users/userIndex.html')
    if request.POST:
        account = request.session['account']
        users = Users.objects.get(account=account)
        name = request.POST['volunteer_name']
        sex = request.POST['sex']
        age = request.POST['age']
        address = request.POST['address']
        cultural_level = request.POST['cultural_level']
        Volunteer.objects.create(volunteer_name=name, sex=sex, age=age, address=address, cultural_level=cultural_level, users=users)
        request.session['ac_points'] = 0
        request.session['av_points'] = 0
        context['ac_points'] = 0
        context['av_points'] = 0
        context['is_manager'] = False
        return render(request,'./Users/userIndex.html', context)
