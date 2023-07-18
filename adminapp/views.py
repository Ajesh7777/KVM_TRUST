from io import BytesIO
from statistics import variance
from tokenize import Number
from venv import create
from django import template
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import get_template

from html.parser import HTMLParser
from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template

from newp import settings #used for calling views in useraapp
from django.shortcuts import render, redirect
from .forms import  ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound
from email.message import EmailMessage
from adminapp.models import * #importing tables

 
# Create your views here.
def home(request):
    wp1=home_wallpaper.objects.get(id=1)
    wp2=home_wallpaper.objects.get(id=2)
    wp3=home_wallpaper.objects.get(id=3)#id possition values will be stored in data
    news1=news_tbl1.objects.all()
    news2=news_tbl2.objects.all()

    gp1=photo_gallery.objects.get(id=1)
    gp2=photo_gallery.objects.get(id=2)
    gp3=photo_gallery.objects.get(id=3)
    gp4=photo_gallery.objects.get(id=4)
    gp5=photo_gallery.objects.get(id=5)
    gp6=photo_gallery.objects.get(id=6)
    gp7=photo_gallery.objects.get(id=7)
    gp8=photo_gallery.objects.get(id=8)
    notif=notifications.objects.all()
    insti=institution_list.objects.all()


        #  data=tbl_login.objects.all()  



    return render(request,'adminapp/home.html',{'wp1':wp1,'wp2':wp2,'wp3':wp3,'news1':news1,'news2':news2,'gp1':gp1,
    'gp2':gp2,'gp3':gp3,'gp4':gp4,'gp5':gp5,'gp6':gp6,'gp7':gp7,'gp8':gp8,'notif':notif,'insti':insti,})


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

def placementcell(request):
    return render(request,'adminapp/placementcell.html')  

def news_events(request):
    return render(request,'adminapp/news_events.html')  

def news1(request,id):
    data1=news_tbl1.objects.get(id=id)
    return render(request,'adminapp/news1.html',{'data1':data1}) 
def news2(request,id):
    data2=news_tbl2.objects.get(id=id)
    return render(request,'adminapp/news2.html',{'data2':data2})  
def notification(request,id):
    data=notifications.objects.get(id=id)
    return render(request,'adminapp/notification.html',{'data':data})  

# def viewmore_news(request,bid):
#     data=news.objects.filter(id=bid)
#     return HttpResponseRedirect(reverse('news1'))

#  <!-- <h4><a href="{%url 'viewmore_news' bid=x.id %}?bid=x.id">{{x.description}}</a></h4> -->





# def all_events(request):
#     return render(request,'adminapp/all_events.html')  
   
    


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 

			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'ajeshmn.767@gmail.com', ['ajeshmn.666@gmail.com']) 

			except BadHeaderError:
				return HttpResponse('Invalid header found.')

      
	form = ContactForm()
    
	return render(request, "adminapp/contact.html", {'form':form})
	

def videogallery(request):
    link=videogallery_link.objects.all()

    return render(request,'adminapp/videogallery.html',{'link':link,})  
def cop_video(request):
    return render(request,'adminapp/cop_video.html')  


def news_letter(request):
    newl=newsletters.objects.all()

    return render(request,'adminapp/news_letter.html',{'newl':newl,})  
def career(request):
    vacancies=careers.objects.all()
    return render(request,'adminapp/career.html',{'vacancies':vacancies,})  
def applictionform(request):
    pdf=appliction_form.objects.all()
    return render(request,'adminapp/applictionform.html',{'pdf':pdf,})  

    

def online_appl(request):
    message=''
    if request.method=='POST':
        a=request.POST.get('fname')
        b=request.POST.get('mname')
        c=request.POST.get('lname')
        d=request.POST.get('gender')
        e=request.POST.get('dob')
        f=request.POST.get('religion')
        g=request.POST.get('caste')
		# nat=request.POST.get('nationality')
        i=request.POST.get('age')
        j=request.POST.get('marital_status')
        k=request.POST.get('blood_group')
        l=request.POST.get('applied_course')
        m=request.POST.get('qualify1')
        n=request.POST.get('institute1')
        o=request.POST.get('year1')
        p=request.POST.get('mark1')
        q=request.POST.get('qualify2')
        r=request.POST.get('institute2')
        s=request.POST.get('year2')
        t=request.POST.get('mark2')
        u=request.POST.get('qualify3')
        v=request.POST.get('institute3')
        w=request.POST.get('year3')
        x=request.POST.get('mark3')
        y=request.POST.get('qualify4')
        z=request.POST.get('institute4')
        ga=request.POST.get('year4')
        gb=request.POST.get('mark4')
        gc=request.POST.get('fathername')
        gd=request.POST.get('fatheroccupation')
        ge=request.POST.get('fatherincome')
        gf=request.POST.get('fatheraddress')
        gg=request.POST.get('fathertel')
        gh=request.POST.get('fathermobile')
        gi=request.POST.get('fatheremail')
        gj=request.POST.get('communication_address')
        gk=request.POST.get('declaration')







        # gm=request.POST.get('send')
        if i!=0:

            # data=create(name=a,age=c,dob=b,address=d,email=e,phone_number=f,gender=g)
            subject='online application form'
            # mailmsg='hi\n your name is '+a+' and your pwd is '+e+'\n Thankyou ' 
            emailfrom=settings.EMAIL_HOST_USER
            rlist=['ajeshmn.666@gmail.com']

            template = get_template('adminapp/online_appl.html')
            context = {
                "billno": a,
                "billdate": b,
                "patientname": c,
                "totalbill": c,
                "billprocedure": d,

            }

            html  = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
            pdf = result.getvalue()
            filename = 'onlineform.pdf'
            # to_emails = ['receiver@gmail.com']
            # subject = "From CliMan"

            email = EmailMessage(subject, "helloji", emailfrom,rlist)
            email.attach(filename, pdf, "application/pdf")
            email.send(fail_silently=False)

            # send_mail(subject,mailmsg,emailfrom,rlist,fail_silently=True)
            message='registration done successfully'
        else:
            message='error occured'
    
    return render(request,'adminapp/online_appl.html',{'message':message})



def online_appl_portal(request):
    return render(request,'adminapp/online_appl_portal.html')  
   


# def online_appl(request):
#     if request.method=='POST':

#         a=request.POST.get('fname')
#         b=request.POST.get('mname')
#         c=request.POST.get('lname')
#         d=request.POST.get('gender')
#         e=request.POST.get('dob')
#         f=request.POST.get('religion')
#         g=request.POST.get('caste')
#         i=request.POST.get('age')
#         j=request.POST.get('marital_status')
#         k=request.POST.get('blood_group')
#         l=request.POST.get('applied_course')
#         m=request.POST.get('qualify1')
#         n=request.POST.get('institute1')
#         o=request.POST.get('year1')
#         gh=request.POST.get('fathermobile')
#         gi=request.POST.get('fatheremail')
#         gj=request.POST.get('communication_address')
#         gk=request.POST.get('declaration')

#         fs = FileSystemStorage()
#         filename = 'online_appl.html'
#         if fs.exists(filename):
#             with fs.open(filename) as pdf:
#                 response = HttpResponse(pdf, content_type='online_appl/pdf')
#                 response['Content-Disposition'] = 'inline; filename="online_appl.pdf"'

#                 subject = 'Welcome to Project Management Portal.'
#                 message = 'Thank you for being part of us. \n We are glad to have you. \n Regards \n Team Project Management'
#         # message.attach = 'filename="mypdf.pdf", content_disposition="inline", data=open("mypdf.pdf", "rb")'
#                 from_email = settings.EMAIL_HOST_USER
#                 to_list = ['ajeshmn.666@gamil.com']
#         # send_mail(subject, message, message.attach, from_email, to_list)

#                 message = message.EmailMessage(subject, message, from_email, to_list)
#         # pdf = open('media/mypdf.pdf', 'rb')
#                 message.attach_file('media/online_appl.pdf')
#                 message.send()

#                 return response
#         else:
#             return HttpResponseNotFound('The requested pdf was not found in our server.')




        