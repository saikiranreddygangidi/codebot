from django.db import models

# Create your models here.
class Reg(models.Model):
    username=models.CharField(max_length=200)
    image= models.ImageField(upload_to='pics')
    password=models.CharField(max_length=200)
class Regi(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)