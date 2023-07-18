from django.shortcuts import render
from django.urls import reverse #used for calling views in useraapp


# Create your views here.
def home(request):
    return render(request,'adminapp/home.html')

def about(request):
    return render(request,'adminapp/about.html')

def msc_nursing(request):
    return render(request,'adminapp/msc_nursing.html')

def bsc_nursing(request):
    return render(request,'adminapp/bsc_nursing.html')

def post_basic_nursing(request):
    return render(request,'adminapp/post_basic_nursing.html')

def bsc_medical_labo(request):
    return render(request,'adminapp/bsc_medical_labo.html')

def diploma_med_lab(request):
    return render(request,'adminapp/diploma_med_lab.html')

def gnm(request):
    return render(request,'adminapp/gnm.html')
def aux_midwife(request):
    return render(request,'adminapp/aux_midwife.html')
def cert_pharma(request):
    return render(request,'adminapp/cert_pharma.html')  
def online_appl(request):
    return render(request,'adminapp/online_appl.html')  


    
  

    



def photogallery(request):
    return render(request,'adminapp/photogallery.html')