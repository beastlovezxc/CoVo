'''
@Author: BeanCB
@Date: 2020-04-25 16:41:48
@LastEditors: BeanCB
@LastEditTime: 2020-04-28 23:43:21
@Description: file content
@FilePath: /Covo/Recourse/views.py
'''
'''
@Author: BeanCB
'''
from django.shortcuts import render
from .models import Recourse
from Users.models import Users
# Create your views here.

def to_recourse(request):
    return render(request, './Recourse/recourse.html')

def record_recourse(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        account = request.session['account']
        users = Users.objects.get(account=account)
        Recourse.objects.create(title=title, text=text, users=users)
        return render(request, './Users/userIndex.html', {'account': account})
    return render(request, './Recourse/recourse.html', {'error': '发布失败'})

# def get_helperlist(request):
#     context = {}
#     context['helperlist'] = Recourse.objects.all().values('helper_number', 'helper_name')
#     return render(request, './Helper/helperlist.html', context)

# def get_helperinfo(request, helper_number):
#     context = {}
#     context['helperinfo'] = Recourse.objects.get(helper_number = helper_number)
#     return render(request, './Helper/helperinfo.html', context)