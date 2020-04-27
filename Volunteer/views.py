'''
@Author: your name
@Date: 2020-04-25 16:41:09
@LastEditTime: 2020-04-28 00:22:59
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

def get_volunteerinfo(request, volunteer_number):
    context = {}
    context['volunteerinfo'] = Volunteer.objects.get(volunteer_number=volunteer_number)
    return render(request, './Volunteer/volunteerinfo.html', context)

def to_setInfo(request):
    return render(request, './Volunteer/to_setInfo.html')

def setInfo(request):
    if request.POST:
        account = request.session['account']
        users = Users.objects.get(account=account)
        name = request.POST['volunteer_name']
        sex = request.POST['sex']
        age = request.POST['age']
        address = request.POST['address']
        cultural_level = request.POST['cultural_level']
        Volunteer.objects.create(volunteer_name=name, sex=sex, age=age, address=address, cultural_level=cultural_level, users=users)
        return render(request,'./Users/userIndex.html')
