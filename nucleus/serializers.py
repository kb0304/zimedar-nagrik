from rest_framework import serializers
from .models import *

class IncidentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Incident
    fields = '__all__'#('lat','lng','timestamp','description','image','is_verification','parent_incident')
