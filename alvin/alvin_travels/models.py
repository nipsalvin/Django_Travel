from django.db import models

# Create your models here.

class Destination(models.Model):
    #id = models.IntegerField. This is not necessary as SQL automatically creates id column 
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()