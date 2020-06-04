from django.shortcuts import render

# Create your views here.
from .models import Feedback
from Users.models import Users
from Activity.models import Activity
from .serializer import FeedbackSerializer,FeedbackSerializer2
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def Feedback_List(request, format=None):
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FeedbackSerializer2(data=request.data)
        print(request.data)
        # print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def Feedback_Join(request, account, feedback):
    try:
        feedback = Feedback.objects.get(account = account, feedback_id = feedback)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedbackSerializer2(feedback, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def Feedback_Detail(request, account):
    try:
        feedback = Feedback.objects.filter(account=account)
        print("feedback")
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FeedbackSerializer(feedback,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("put12312312312312321")
        serializer = FeedbackSerializer(feedback, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)