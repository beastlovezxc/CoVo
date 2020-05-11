'''
@Author: BeanCB
@Date: 2020-04-25 16:42:26
@LastEditors: BeanCB
@LastEditTime: 2020-05-12 02:32:31
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
from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from .models import Walfare
from Users.models import Users
from Volunteer.models import Volunteer
# Create your views here.
def get_walfarelist(request):
    context = {}
    context['account'] = request.session['account']
    context['is_manager'] = False
    context['av_points'] = request.session['av_points']
    context['ac_points'] = request.session['ac_points']
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


def exchange(request, prize_number):
    user = Users.objects.get(account = request.session['account'])
    vo_info = user.volunteer_set.all().get(users=user)
    prize = Walfare.objects.get(prize_number=prize_number)
    if vo_info.available_points < prize.prize_points:
        return HttpResponse('剩余积分不足，无法兑换！')
    vo_info.available_points -= prize.prize_points
    vo_info.save()
    request.session['av_points'] = vo_info.available_points
    return HttpResponse('兑换成功')