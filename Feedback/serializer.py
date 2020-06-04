from rest_framework import serializers
from .models import Feedback
from Users.models import Users
from Activity.models import Activity

class FeedbackSerializer(serializers.ModelSerializer):
    users_name = serializers.ReadOnlyField()
    activity_name = serializers.ReadOnlyField()
    class Meta:
        model = Feedback
        fields = ('users_name','activity_name','feedback', 'time', 'feedback_id')

class FeedbackSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('account','activity_number','feedback', 'time', 'feedback_id')