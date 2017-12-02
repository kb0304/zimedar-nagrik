from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from django.conf import settings
from rest_framework.response import Response

from .function import getMinistry
from .serializers import *
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

class VerifyView(generics.ListCreateAPIView):
  queryset = Verify.objects.all()
  serializer_class = VerifySerializer

  def create(self, request, *args, **kwargs):
    incidentId = request.data.get('incident','')
    response = request.data.get('response','')
    try:
      incident = Incident.objects.get(id=incidentId)
    except Exception as e:
      return Response({"message":"Incident not valid"})
    if(response not in [1,2,3]):
      return Response({"message":"Response code not valid"})
    if(incident.reported):
        return Response({"message":"Already Repored"})
    if(response==1 and incident.verify.filter(response=1).count()-incident.verify.filter(response=2).count()>=2):
        incident.reported = True
        ministry = getMinistry(incident.description)
        incident.ministry = ministry
        incident.save()
        print('Incident reported - '+str(incident.id)+' description: '+incident.description+' to ministry: '+incident.ministry)
    if(response==1):
        response = "Yes"
    elif(response==2):
        response = "No"
    else:
        resonse = "Not Sure"
    return super(VerifyView, self).create(request, *args, **kwargs)

def index(request):
    return render(request, 'index.html', {})
