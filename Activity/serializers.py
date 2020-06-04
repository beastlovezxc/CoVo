from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_number', 'activity_name', 'introduction', 'expired', 'required_num', 'participants', 'address', 'activity_points', 'date', 'contact')