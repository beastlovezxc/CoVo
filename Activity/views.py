'''
@Author: your name
@Date: 2020-04-25 16:41:21
@LastEditTime: 2020-05-25 01:09:12
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: /Covo/Activity/views.py
'''
from django.shortcuts import render
from .models import Activity
from .serializers import ActivitySerializer
# from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def Activity_List(request, format=None):
    if request.method == 'GET':
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Activity_Detail(request, activity_number):
    try:
        activity = Activity.objects.get(activity_number=activity_number)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = ActivitySerializer(activity, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class VolunteerList(APIView):
    def get(self, request, format=None):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VolunteerDetail(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(users=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    context['activitylist'] = Activity.objects.all().values('activity_number', 'activity_name', 'date')
    context['is_manager'] = request.session['is_manager']
    return render(request, './Activity/activitylist.html', context)

def show_activityinfo(request, activity_number):
    context = {}
    context['activityinfo'] = Activity.objects.get(activity_number=activity_number)
    return render(request, './Activity/activityinfo.html', context)