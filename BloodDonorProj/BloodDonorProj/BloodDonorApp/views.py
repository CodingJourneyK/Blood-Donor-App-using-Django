from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from BloodDonorApp.models import Donor, DonorForm
#from BloodDonorApp.forms import DonorForm

# Create your views here.

#views: base template
def home(request):
    return render(request,'index.html',{})

#create donor
def createDonor(request):
    if request.method=='POST':
        form=DonorForm(request.POST)
        if form.is_valid():
            newdnr=form.save() #form inuput save
            newdnr.save() #ddb table (admin) save   
        return render(request,"donorFrm.html",   
                      {'newdonor':newdnr,'form':DonorForm()})
    else:
        return render(request,'donorFrm.html',{'form':DonorForm()})

#read all donors
def donorList(request):
    dnr=Donor.objects.all()
    return render(request,'listall.html',{'donors':dnr})

#search a donor by phone number
def search(request):
    if request.method == 'POST':
        dphone=request.POST['phone']
        dnr=Donor.objects.filter(phone__contains=dphone)
        return render(request,'donorSearch.html',{'results':dphone,'donors':dnr})
    else:
        return render(request,'donorSearch.html',{})
