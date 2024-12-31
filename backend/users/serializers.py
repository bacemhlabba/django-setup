# serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Company, Director, HistoricalChange

User = get_user_model()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class HistoricalChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalChange
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True, read_only=True)
    history = HistoricalChangeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'