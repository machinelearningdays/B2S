from rest_framework import serializers
from .models import FoodRemainingTimes, Emergency, FoodStatus, FoodOrNot


class FoodRemainingTimesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodRemainingTimes
        fields = '__all__'


class EmergencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'


class FoodStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodStatus
        fields = '__all__'


class FoodOrNotSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodOrNot
        fields = '__all__'
