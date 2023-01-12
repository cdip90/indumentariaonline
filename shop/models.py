from django.db import models

# Create your models .

class Remeras (models.Model):
    marca = models.CharField(max_length=50)
    talle = models.IntegerField()
    color = models.CharField(max_length= 20)
    lisa = models.BooleanField()
    genero = models.IntegerField()

