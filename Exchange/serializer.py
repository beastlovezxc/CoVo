from rest_framework import serializers
from .models import Exchange
from Users.models import Users

class ExchangeSerializer(serializers.ModelSerializer):
    users_name = serializers.ReadOnlyField()
    prize_name = serializers.ReadOnlyField()
    voinfo_name = serializers.ReadOnlyField()
    class Meta:
        model = Exchange
        fields = ('users_name','prize_name','voinfo_name','exchange_time', 'exchange_number', 'exchanged')

# class ExchangeSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Exchange
#         fields = ('account','activity_number', 'voinfo','status', 'apply_id')