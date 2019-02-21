from django.db import models

# Create your models here.

#my model Car that askes for make model and year
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
