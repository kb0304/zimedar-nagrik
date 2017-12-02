from django.db import models

class Incident(models.Model):
#  reported = models.ForeignKey(to=User)
  lat = models.DecimalField(max_digits=10,decimal_places=8)
  lng = models.DecimalField(max_digits=10,decimal_places=8)
  timestamp = models.DateTimeField(auto_now_add=True)
  description = models.TextField()
  image = models.ImageField(upload_to='incidents/')
  reported = models.BooleanField(default=False)

RESPONSE_CHOICES = (
  (1,'Yes'),
  (2,'No'),
  (3,'Not Sure'),
)
class Verify(models.Model):
  incident = models.ForeignKey(to=Incident,on_delete=models.CASCADE, related_name='verify')
  response = models.IntegerField(choices=RESPONSE_CHOICES)
#  user = models.ForeignKey(to=User)
