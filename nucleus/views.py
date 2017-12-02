from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from django.conf import settings

from .serializers import IncidentSerializer
from .models import *

# Create your views here.
class IncidentView(generics.ListCreateAPIView):
  def get_queryset(self):
    request = self.request
    try:
      lat = float(request.GET.get('lat',''))
      lng = float(request.GET.get('lng',''))
      if lat and lng:
        return Incident.objects.filter(lat__gte=lat-settings.LAT_FACTOR, lat__lte=lat+settings.LAT_FACTOR, lng__gte=lng-settings.LAT_FACTOR, lng__lte=lng+settings.LAT_FACTOR)
    except Exception as e:
        return Incident.objects.all()    
    return Incident.objects.all()
  serializer_class = IncidentSerializer
