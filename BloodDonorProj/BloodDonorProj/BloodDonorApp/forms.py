'''
#forms.py
from django import forms


Blood_Choices=(
    ("1","A+ve"),
    ("2","B+ve"),
    ("3","O+ve"),
    ("4","AB+ve"),
    ("5","A-ve"),
    ("6","B-ve"),
    ("7","O-ve"),
    ("8","AB-ve")    
     )
Gender_Choice=[('M','Male'),('F','Female')]

class DonorForm(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    gender=forms.CharField(label='Gender',
                           widget=forms.RadioSelect(choices=Gender_Choice))
    blood=forms.ChoiceField(choices=Blood_Choices)
    phone=forms.CharField(max_length=10)
    address=forms.CharField(widget=forms.Textarea)
    
    
'''
