from django.db import models

# Create your models here.
class Event(models.Model):
    '''event model class'''
    event_text = models.TextField(max_length=600)
