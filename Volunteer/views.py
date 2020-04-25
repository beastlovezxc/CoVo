'''
@Author: your name
@Date: 2020-04-25 16:41:09
@LastEditTime: 2020-04-25 19:27:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Covo/Volunteer/views.py
'''
from django.shortcuts import render
from .models import Volunteer
# Create your views here.
def get_volunteerlist(request):
    context = {}
    context['volulist'] = Volunteer.objects.all().values('volunteer_number','volunteer_name')
    return render(request, './Volunteer/volunteerlist.html', context)

def get_volunteerinfo(request, volunteer_number):
    context = {}
    context['volunteerinfo'] = Volunteer.objects.get(volunteer_number=volunteer_number)
    return render(request, './Volunteer/volunteerinfo.html', context)