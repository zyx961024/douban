from django.db import models

# Create your models here.
class Movie(models.Model):
    pic = models.CharField(max_length=80)
    name= models.CharField(max_length=80)
    director = models.CharField(max_length=80)
    star = models.CharField(max_length=80)
    comment = models.CharField(max_length=80)
class User(models.Model):
    username=models.CharField(max_length=80)
    password=models.CharField(max_length=80)
    phone=models.CharField(max_length=80)