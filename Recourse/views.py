'''
@Author: FengSiJia
@Date: 2020-04-25 16:41:48
@LastEditors: FengSiJia
@LastEditTime: 2020-06-06 02:18:23
@Description: file content
@FilePath: \Covo\Recourse\views.py
'''
'''
@Author: FengSiJia
'''
from django.shortcuts import render
from .models import Recourse
from Users.models import Users
from .serializer import RecourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def Recourse_List(request, format=None):
    if request.method == 'GET':
        recourese = Recourse.objects.all()
        serializer = RecourseSerializer(recourese, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecourseSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Recourse_Detail(request, index):
    try:
        recourese = Recourse.objects.get(index=index)
    except Recourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RecourseSerializer(recourese)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = RecourseSerializer(recourese, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recourese.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def MyRecourse_List(request, account, format=None):
    if request.method == 'GET':
        recourese = Recourse.objects.filter(users=account)
        serializer = RecourseSerializer(recourese, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecourseSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def MyRecourse_Detail(request, account):
    try:
        recourese = Recourse.objects.get(users=account)
    except Recourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RecourseSerializer(recourese)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = RecourseSerializer(recourese, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        recourese.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def to_recourse(request):
    return render(request, './Recourse/recourse.html')

def record_recourse(request):
    if request.POST:
        title = request.POST['title']
        text = request.POST['text']
        account = request.session['account']
        users = Users.objects.get(account=account)
        Recourse.objects.create(title=title, text=text, users=users)
        return render(request, './Users/userIndex.html', {'account': account, 'is_manager': users.manager})
    return render(request, './Recourse/recourse.html', {'error': '发布失败'})

def show_list(request):
    context = {}
    context['recourse_list'] = Recourse.objects.all().values('index','title', 'time', 'users')
    print(context['recourse_list'])
    return render(request, './Recourse/show_list.html', context)
# def get_helperlist(request):
#     context = {}
#     context['helperlist'] = Recourse.objects.all().values('helper_number', 'helper_name')
#     return render(request, './Helper/helperlist.html', context)

# def get_helperinfo(request, helper_number):
#     context = {}
#     context['helperinfo'] = Recourse.objects.get(helper_number = helper_number)
#     return render(request, './Helper/helperinfo.html', context)