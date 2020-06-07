from rest_framework import serializers
from .models import Walfare


class WalfareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walfare
        fields = ('prize_number','prize_name','prize_points', 'prize_introduction', 'prize_image')