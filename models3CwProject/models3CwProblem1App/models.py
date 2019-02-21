from django.db import models
from django.utils import timezone

# Create your models here.



#model for book that asks for page , genre and publish date
class Book(models.Model):
    page_number= models.IntegerField()
    genre = models.CharField(max_length=100)
    publish_date = models.DateField(default=timezone.now())



















