from django.db import models

class Incident(models.Model):
#  reported_by = models.ForeignKey(to=User)
  lat = models.DecimalField(max_digits=10,decimal_places=8)
  lng = models.DecimalField(max_digits=10,decimal_places=8)
  timestamp = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  image = models.ImageField(upload_to='incidents/')
  is_verification = models.BooleanField(default=False)
  parent_incident = models.ForeignKey("self",blank=True, null=True,on_delete=models.CASCADE)
