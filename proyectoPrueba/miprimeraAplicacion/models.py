from django.db import models

# Create your models here.

class TejidoMama (models.Model):
    partP = models.IntegerField()
    temperatura = models.FloatField()
    color = models.FloatField()
    inflamacion = models.FloatField()
    

