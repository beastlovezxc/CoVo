from rest_framework import serializers
from .models import Apply
from Users.models import Users
from Activity.models import Activity

class ApplySerializer(serializers.ModelSerializer):
    users_name = serializers.ReadOnlyField()
    activity_name = serializers.ReadOnlyField()
    class Meta:
        model = Apply
        fields = ('users_name','activity_name','status')

class ApplySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ('account','activity_number','status')