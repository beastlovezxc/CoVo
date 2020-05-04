'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-05-03 17:15:10
@Description: file content
@FilePath: /Covo/Walfare/views.py
'''
'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-05-01 00:50:42
@Description: file content
@FilePath: /Covo/Walfare/views.py
'''
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Walfare
# Create your views here.
def get_walfarelist(request):
    context = {}
    context['walfarelist'] = Walfare.objects.all().values('prize_number','prize_name', 'prize_points')
    return render(request, './Walfare/walfarelist.html', context)

def to_walfaremanager(request):
    context = {}
    context['walfarelist'] = Walfare.objects.all().values('prize_number','prize_name', 'prize_points')
    # redirect('/Walfare/to_walfaremanager/')
    return render(request, './Walfare/walfaremanager.html', context)

def add_walfare(request):
    return render(request, './Walfare/add_walfare.html')

def save_walfare(request):
    if request.POST:
        if request.POST['prize_number'] is not 0:
            prize_name = request.POST['name']
            prize_introduction = request.POST['introduction']
            prize_points = request.POST['points']
            Walfare.objects.create(prize_name=prize_name, prize_introduction=prize_introduction, prize_points=prize_points)
        else:
            prize_number = request.POST['prize_number']
            walfare = Walfare.objects.get(prize_number=prize_number)
            walfare.prize_name = request.POST['name']
            walfare.prize_introduction = request.POST['introduction']
            walfare.prize_points = request.POST['points']
            walfare.save()
        # return to_walfaremanager(request)
        return redirect('/walfare/to_walfaremanager/')

def edit_walfare(request, prize_number):
    context = {}
    context['walfareinfo'] = Walfare.objects.get(prize_number=prize_number)
    return render(request, './Walfare/edit_walfare.html', context)

def delete_walfare(request, prize_number):
    Walfare.objects.get(prize_number=prize_number).delete()
    return to_walfaremanager(request)

def get_walfareinfo(request, prize_number):
    context = {}
    context['walfareinfo'] = Walfare.objects.get(prize_number=prize_number)
    return render(request, './Walfare/walfareinfo.html', context)