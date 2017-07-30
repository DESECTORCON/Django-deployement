from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150,unique=True)
    height = models.IntegerField(max_length=100,unique=True)
    live = models.TextField(max_length=100)
