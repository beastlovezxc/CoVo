from rest_framework import serializers
from .models import Apply
from Users.models import Users
from Activity.models import Activity

class ApplySerializer(serializers.ModelSerializer):
    users_name = serializers.ReadOnlyField()
    activity_name = serializers.ReadOnlyField()
    voinfo_name = serializers.ReadOnlyField()
    class Meta:
        model = Apply
        fields = ('users_name','activity_name','voinfo_name','status', 'apply_id')

class ApplySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ('account','activity_number', 'voinfo','status', 'apply_id')