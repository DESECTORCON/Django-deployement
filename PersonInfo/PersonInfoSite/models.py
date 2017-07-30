from django.db import models

# Create your models here.
class Person(models.Model):
    '''asdfasdf'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150,unique=True)
    height = models.IntegerField(max_length=200,unique=True)
    age = models.IntegerField(max_length=200,default=10)
