from rest_framework import serializers
from .models import Recourse

class RecourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recourse
        fields = ('index', 'title', 'text', 'time', 'status', 'activity_num', 'users')