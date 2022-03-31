from rest_framework import serializers
from .models import ZombieSurvivalSocialNetwork

class ZssnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZombieSurvivalSocialNetwork
        fields = '__all__'
