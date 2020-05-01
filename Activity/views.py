'''
@Author: your name
@Date: 2020-04-25 16:41:21
@LastEditTime: 2020-05-02 00:18:46
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Activity/views.py
'''
from django.shortcuts import render
from .models import Activity
# Create your views here.
def to_recruit(request):
    return render(request, './Activity/to_recruit.html')
    
def recruit(request):
    if request.POST:
        name = request.POST['name']
        introduction = request.POST['introduction']
        required = request.POST['required']
        address = request.POST['address']
        contact = request.POST['contact']
        date = request.POST['date']
        date = date.replace('T', ' ')
        print(date)
        points = request.POST['points']
        # Recourse.objects.create(title=title, text=text, users=users)
        Activity.objects.create(activity_name=name, introduction=introduction, required_num=required, address=address, date=date, activity_points=points, contact=contact)
    return render(request, './Users/userIndex.html',{'account': request.session['account'],'is_login': request.session['is_login'], 'is_manager': request.session['is_manager']})

def activitylist(request):
    context = {}
    
    context['activitylist'] = Activity.objects.all().values('activity_number', 'activity_name')
    return render(request, './Activity/activitylist.html', context)

def show_activityinfo(request, activity_number):
    context = {}
    context['activityinfo'] = Activity.objects.get(activity_number=activity_number)
    return render(request, './Activity/activityinfo.html', context)