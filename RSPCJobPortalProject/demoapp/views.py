from django.shortcuts import render
from demoapp.models import *


# Create your views here.
# now we want to display data presrnt in model class to the end user (html page)
def index_view(request):
    return render(request,"demoapp/index.html")

def PuneJobs_view(request):
    pjobs=PuneJobs.objects.all()#django-ORM
    return render(request,"demoapp/punejob.html",{'pjobs':pjobs})

def BangloreJobs_view(request):
    bjobs=BangloreJobs.objects.all()#django-ORM
    return render(request,"demoapp/banglorejob.html",{'bjobs':bjobs})

def ChennaiJobs_view(request):
    cjobs=ChennaiJobs.objects.all()#django-ORM
    return render(request,"demoapp/chennaijob.html",{'cjobs':cjobs})

def HydrabadJobs_view(request):
    hjobs=HydrabadJobs.objects.all()#django-ORM
    return render(request,"demoapp/hydrabad.html",{'hjobs':hjobs})
