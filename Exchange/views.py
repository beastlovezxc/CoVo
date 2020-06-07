'''
@Author: FengSiJia
@Date: 2020-04-25 16:42:35
@LastEditors: FengSiJia
@LastEditTime: 2020-04-25 21:47:32
@Description: file content
@FilePath: /Covo/Exchange/views.py
'''
from django.shortcuts import render
from .models import Exchange
# Create your views here.
from Users.models import Users
from .serializer import ExchangeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def Exchange_List(request, format=None):
    if request.method == 'GET':
        exchange = Exchange.objects.all()
        serializer = ExchangeSerializer(exchange, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExchangeSerializer(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Exchange_Detail(request, account):
    try:
        exchange = Exchange.objects.filter(account=account)
        print("exchange")
    except Exchange.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ExchangeSerializer(exchange,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = ExchangeSerializer(exchange, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        exchange.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_exchangelist(request):
    context = {}
    context['exchangelist'] = Exchange.objects.all()
    return render(request, './Exchange/exchange.html', context)