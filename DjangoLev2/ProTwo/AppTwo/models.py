from django.db import models

# Create your models here.
class First_Name(models.Model):
    firstName = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.firstName

class Last_Name(models.Model):
    firstName = models.ForeignKey(First_Name)
    lastName = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.lastName

class Email(models.Model):
    lastname = models.ForeignKey(Last_Name)
    email = models.EmailField()

    def __str__(self):
        return self.email
