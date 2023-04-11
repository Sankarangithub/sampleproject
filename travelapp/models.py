from django.db import models

# Create your models here.
class Destinations(models.Model):
    destinationName=models.CharField(max_length=15)
    destinationDescription=models.TextField(max_length=100)
    destinationPrize=models.IntegerField()
    destinationImage=models.ImageField(upload_to='img',default='null.jpg')

class Register(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)
    Phone=models.IntegerField()
    
    
    