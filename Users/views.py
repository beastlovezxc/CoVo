
# @Author: your name
# @Date: 2020-04-25 16:40:36
# @LastEditTime: 2020-06-02 23:21:52
# @LastEditors: BeanCB
# @Description: In User Settings Edit
# @FilePath: \Covo\Users\views.py

import time
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from . import models
from Volunteer.models import Volunteer
from rest_framework import viewsets
from Users.serializer import UsersSerializer
# Create your views here.

@api_view(['GET','POST'])
def User_List(request, format=None):
    if request.method == 'GET':
        users = models.Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def User_Detail(request, account):
    try:
        user = models.Users.objects.get(account=account)
    except models.Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AuthView(APIView):

    def post(self,request,*args,**kwargs):

        ret = {'status':0,'msg':None}
        try:
            # 参数是datadict 形式
            usr = request.data.get('account')
            pas = request.data.get('password')

            print(usr)
            print(pas)
            obj = models.Users.objects.filter(account=usr,password=pas).first()
            print(obj)
            print(type(obj))
            print(obj.account)
            print(obj.password)
            print(1234)
            if not obj:
                ret['status'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
            # 里为了简单，应该是进行加密，再加上其他参数
            token = str(time.time()) + usr
            print(token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            ret['manager'] = obj.manager
            #ret['token'] = token
        except Exception as e:
            print(e)
            ret['status'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)

# 用户登录
# 比对users表中的用户名和密码
# 不一致则返回Covo/index
# 一致则进入用户主页 userIndex中
# 且session记录登录状态
def login(request):
    if request.POST:
        account = request.POST['account']
        password = request.POST['password']
        is_user = models.Users.objects.filter(account = account)
        if not is_user:
            return render(request, './Covo/index.html', {'error': '用户名不存在!'})
        user = models.Users.objects.get(account = account)
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
        user = models.Users.objects.filter(account = account)
        if user:
            return render(request, './Users/regist.html', {'error' : '用户名已存在!'})
        user = models.Users.objects.create(account = account, password = password, manager = 0)
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
    queryset = models.Users.objects.all()
    serializer_class = UsersSerializer