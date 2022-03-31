from django.db import models

def locationdata():
    return {"latitude": "0.0.0",
            "longitude": "0.0.0"}

class ZombieSurvivalSocialNetwork(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField(default = None)
    gender = models.CharField(max_length=30)
    location = models.JSONField('Location',default = locationdata)
    infected = models.BooleanField(default='False')
    