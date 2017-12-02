from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics

from .serializers import IncidentSerializer
from .models import *

# Create your views here.
class IncidentView(generics.ListCreateAPIView):
  queryset = Incident.objects.all()
  serializer_class = IncidentSerializer

def get_nearby(lat, lng):
  return Incident.objects.filter(lat__gte=lat-0.0001, lat__sme=lat+0.0001, lng__gte=lng-0.0001, lng__sme=lng+0.0001)

