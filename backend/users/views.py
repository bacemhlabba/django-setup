# views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from django.contrib.auth import get_user_model
from .permissions import AllowAny 
from rest_framework import viewsets
from .models import Company, Director, HistoricalChange
from .serializers import DirectorSerializer, HistoricalChangeSerializer, CompanySerializer
from django_filters.rest_framework import DjangoFilterBackend




class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'uid', 'headquarters']

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class HistoricalChangeViewSet(viewsets.ModelViewSet):
    queryset = HistoricalChange.objects.all()
    serializer_class = HistoricalChangeSerializer