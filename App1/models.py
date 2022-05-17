from calendar import c
from pickle import TRUE
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Ticket(models.Model):
    Department=models.CharField(max_length=100)
    Category= models.CharField(max_length=100)
    VegaOps_GitLab_Project_URL=models.CharField(max_length=500)
    Subject=models.CharField(max_length=500)
    Description=models.CharField(max_length=1000)
    Contact_Name=models.CharField(max_length=100) 
    Email=models.CharField(max_length=100)
    Phone=models.CharField(max_length=15)
   
    upload_file = models.FileField(upload_to='files')    
    upload_date = models.DateTimeField()
    def __str__(self):
        return self.Department