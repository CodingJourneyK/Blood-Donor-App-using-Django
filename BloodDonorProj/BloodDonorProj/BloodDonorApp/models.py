from django.db import models
from django import forms

# Create your models here.
Gender_Choices=[('Male','MALE'),('Female','FEMALE')]
Blood_Choices=[
    ("1","A+ve"),
    ("2","B+ve"),
    ("3","O+ve"),
    ("4","AB+ve"),
    ("5","A-ve"),
    ("6","B-ve"),
    ("7","O-ve"),
    ("8","AB-ve")    
     ]
class Donor(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=6,choices=Gender_Choices)
    blood=models.CharField(max_length=5,choices=Blood_Choices)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    class Meta:
        db_table='donortbl'

class DonorForm(forms.ModelForm):
    class Meta:
        model=Donor
        fields='__all__'
        widgets={'gender':forms.RadioSelect(choices=Gender_Choices)}
