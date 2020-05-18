'''
@Author: your name
@Date: 2020-04-25 16:40:36
@LastEditTime: 2020-05-18 00:14:31
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Users/views.py
'''
from django.shortcuts import render
from .models import Users
from Volunteer.models import Volunteer
from rest_framework import viewsets
from Users.serializer import UsersSerializer
# Create your views here.

# 用户登录
# 比对users表中的用户名和密码
# 不一致则返回Covo/index
# 一致则进入用户主页 userIndex中
# 且session记录登录状态
def login(request):
    if request.POST:
        account = request.POST['account']
        password = request.POST['password']
        is_user = Users.objects.filter(account = account)
        if not is_user:
            return render(request, './Covo/index.html', {'error': '用户名不存在!'})
        user = Users.objects.get(account = account)
        print(password)
        print(user.password)
        if user.password != password:
            return render(request, './Covo/index.html', {'error': '密码错误!'})
        request.session['is_login'] = True
        request.session['account'] = account
        vo_info_list = user.volunteer_set.all()
        if vo_info_list:
            vo_info = vo_info_list.get(users=user)
            if vo_info:
                request.session['av_points'] = vo_info.available_points
                request.session['ac_points'] = vo_info.activity_points
            else:
                request.session['av_points'] = 0
                request.session['ac_points'] = 0
        request.session['is_manager'] = user.manager
        context = {}
        context['account'] = account
        context['is_manager'] = user.manager
        context['is_login'] = True
        context['av_points'] = request.session['av_points'] = 0
        context['ac_points'] = request.session['ac_points'] = 0
        return render(request, './Users/userIndex.html', context)
def index(request):
    if request.session['account'] and request.session['is_login']:
        account = request.session['account']
        manager = request.session['is_manager']
        ac_points = request.session['ac_points']
        av_points = request.session['av_points']
        return render(request, './Users/userIndex.html', {'account': account, 'is_manager': manager, 'ac_points': ac_points, 'av_points': av_points})
    return render(request, './Covo/index.html')
# 用户登出
# session删除用户登录状态
# 返回Covo/index
def logout(request):
    if 'is_login' in request.session:
        del request.session['is_login']
        del request.session['account']
        del request.session['is_manager']
        del request.session['ac_points']
        del request.session['av_points']
    return render (request, './Covo/index.html')

# 用户注册跳转
def to_regist(request):
    return render(request, "./Users/regist.html")

# 用户注册
def regist(request):
    if request.POST:
        account = request.POST['account']
        password = request.POST['password']
        user = Users.objects.filter(account = account)
        if user:
            return render(request, './Users/regist.html', {'error' : '用户名已存在!'})
        user = Users.objects.create(account = account, password = password, manager = 0)
        user.save()
        request.session['is_login'] = True
        request.session['account'] = account
        request.session['is_manager'] = False
        request.session['ac_points'] = 0
        request.session['av_points'] = 0
        return render(request, './Users/userIndex.html', {'account': account, 'is_manager': False})
    return render(request, './Users/regist.html')
def show_userlist(request):
    context = {}
    context['userlist'] = Users.objects.all()
    return render(request, './Users/userlist.html', context)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer