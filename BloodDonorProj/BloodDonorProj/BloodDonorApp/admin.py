from django.contrib import admin
from BloodDonorApp import models
#from BloodDonorApp import forms


# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display=('name','blood','age','phone',)

admin.site.register(models.Donor,DonorAdmin)
#admin.site.register(forms.DonorForm,DonorAdmin)

