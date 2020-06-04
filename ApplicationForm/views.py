'''
@Author: BeanCB
@Date: 2020-04-25 16:41:36
@LastEditors: BeanCB
@LastEditTime: 2020-05-03 00:56:24
@Description: file content
@FilePath: /Covo/ApplicationForm/views.py
'''
from django.shortcuts import render,HttpResponse
from .models import Apply
from Users.models import Users
from Activity.models import Activity
from .serializer import ApplySerializer,ApplySerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def Apply_List(request, format=None):
    if request.method == 'GET':
        apply = Apply.objects.all()
        serializer = ApplySerializer(apply, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApplySerializer2(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def Apply_Join(request, account, activity_number):
    try:
        apply = Apply.objects.get(account = account, activity_number = activity_number)
    except Apply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApplySerializer(apply)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApplySerializer2(apply, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def Apply_Detail(request, account):
    try:
        apply = Apply.objects.filter(account=account)
        print("apply")
    except Apply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ApplySerializer(apply,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = ApplySerializer(apply, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def apply(request,activity_number):
    account = request.session['account']
    user = Users.objects.get(account=account)
    activity = Activity.objects.get(activity_number=activity_number)
    if activity.required_num == activity.participants:
        return HttpResponse('人数已满')
    ap = Apply.objects.all().filter(account=user, activity_number=activity)
    if not ap:
        ap = Apply.objects.create(account=user, activity_number=activity)
        ap.save()
        return HttpResponse('已成功报名')
    return HttpResponse('您已经报过名了')