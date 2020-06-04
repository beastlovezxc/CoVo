'''
@Author: your name
@Date: 2020-04-25 16:41:09
@LastEditTime: 2020-06-04 23:34:46
@LastEditors: BeanCB
@Description: In User Settings Edit
@FilePath: \Covo\Volunteer\views.py
'''
from django.shortcuts import render
from .models import Volunteer
from Users.models import Users
from .serializers import VolunteerSerializer
from .serializer import VolunteerSerializers
# from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
# Create your views here.

@api_view(['GET','POST'])
def Volunteer_List(request, format=None):
    if request.method == 'GET':
        volunteer = Volunteer.objects.all()
        serializer = VolunteerSerializers(volunteer, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VolunteerSerializers(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Volunteer_Detail(request, account):
    try:
        volunteer = Volunteer.objects.get(users=account)
    except Volunteer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VolunteerSerializers(volunteer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = VolunteerSerializers(volunteer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class VolunteerList(APIView):
    def get(self, request, format=None):
        volunteer = Volunteer.objects.all()
        serializer = VolunteerSerializer(volunteer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VolunteerDetail(APIView):
    def get_object(self, pk):
        try:
            return Volunteer.objects.get(users=pk)
        except Volunteer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        volunteer = self.get_object(pk)
        serializer = VolunteerSerializer(volunteer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        volunteer = self.get_object(pk)
        serializer = VolunteerSerializer(volunteer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        volunteer = self.get_object(pk)
        volunteer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_volunteerlist(request):
    context = {}
    context['volulist'] = Volunteer.objects.all().values('volunteer_number','volunteer_name', 'users')
    return render(request, './Volunteer/volunteerlist.html', context)

def get_volunteerinfo(request, account):
    context = {}
    print(account)
    user = Users.objects.get(account=account)
    vo_info = user.volunteer_set.all().get(users=user)
    if vo_info:
        context['volunteerinfo'] = vo_info
        return render(request, './Volunteer/volunteerinfo.html', context)
    else:
        return render(request, './Volunteer/to_setInfo.html')

def to_setInfo(request):
    return render(request, './Volunteer/to_setInfo.html', context)

def setInfo(request):
    context = {}
    vo_info = Volunteer.objects.get(volunteer_number=volunteer_number)
    if vo_info:
        request.session['ac_points'] = vo_info.activity_points
        request.session['av_points'] = vo_info.available_points
        context['ac_points'] = vo_info.activity_points
        context['av_points'] = vo_info.available_points
        context['is_manager'] = False
        return render(request,'./Users/userIndex.html')
    if request.POST:
        account = request.session['account']
        users = Users.objects.get(account=account)
        name = request.POST['volunteer_name']
        sex = request.POST['sex']
        age = request.POST['age']
        address = request.POST['address']
        cultural_level = request.POST['cultural_level']
        Volunteer.objects.create(volunteer_name=name, sex=sex, age=age, address=address, cultural_level=cultural_level, users=users)
        request.session['ac_points'] = 0
        request.session['av_points'] = 0
        context['ac_points'] = 0
        context['av_points'] = 0
        context['is_manager'] = False
        return render(request,'./Users/userIndex.html', context)
