'''
@Author: your name
@Date: 2020-04-25 16:40:36
@LastEditTime: 2020-04-26 23:07:50
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Users/views.py
'''
from django.shortcuts import render
from .models import Users
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
        user = Users.objects.filter(account = account)
        if not user:
            return render(request, './Covo/index.html', {'error': '用户名不存在!'})
        user = Users.objects.filter(password = password)
        if not user:
            return render(request, './Covo/index.html', {'error': '密码错误!'})
        request.session['is_login'] = True
        return render(request, './Users/userIndex.html', {'account': account})

# 用户登出
# session删除用户登录状态
# 返回Covo/index
def logout(request):
    if 'is_login' in request.session:
        del request.session['is_login']
    render (request, './Covo/index.html')

def show_userlist(request):
    context = {}
    context['userlist'] = Users.objects.all()
    return render(request, './Users/userlist.html', context)