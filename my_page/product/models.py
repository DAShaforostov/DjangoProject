from django.db import models

# Create your models here.
class Product(models.Model):
    title      = models.CharField(max_lenght=120)
    dicription = models.TextField()
    price      = models.TextField()

