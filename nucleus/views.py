from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics

from .serializers import IncidentSerializer
from .models import *

# Create your views here.
class IncidentView(generics.ListCreateAPIView):
  queryset = Incident.objects.all()
  serializer_class = IncidentSerializer 
