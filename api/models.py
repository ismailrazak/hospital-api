from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user",null=True,blank=True)
    doctor_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="doctor", null=True, blank=True)

    def __str__(self):
         return self.username

class Patient_Records(models.Model):
    patient_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient_records")
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.CharField(max_length=200)
    observations = models.CharField(max_length=500)
    treatments = models.CharField(max_length=400)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name="patient_records")
    misc = models.CharField(max_length=200,null=True,blank=True)
    doctor_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,related_name = "patient_records_doctor",null=True,blank=True)



    def __str__(self):
        return self.diagnostics



