"""newp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path
from adminapp.views import *
from django.urls import include,re_path
from django.conf.urls.static import static 

from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
            re_path(r'^$',home,name='home'),
            re_path(r'^about/$',about,name='about'),
                    re_path(r'^notification/(?P<id>[0-9]+)',notification,name='notification'),

                    re_path(r'^msc_nursing/$',msc_nursing,name='msc_nursing'),
                    re_path(r'^bsc_nursing/$',bsc_nursing,name='bsc_nursing'),
                    re_path(r'^post_basic_nursing/$',post_basic_nursing,name='post_basic_nursing'),
                        re_path(r'^bsc_medical_labo/$',bsc_medical_labo,name='bsc_medical_labo'),
                        re_path(r'^diploma_med_lab/$',diploma_med_lab,name='diploma_med_lab'),
                            re_path(r'^gnm/$',gnm,name='gnm'),
                            re_path(r'^aux_midwife/$',aux_midwife,name='aux_midwife'),

                                 re_path(r'^cert_pharma/$',cert_pharma,name='cert_pharma'),

                                    re_path(r'^online_appl/$',online_appl,name='online_appl'),
                                        re_path(r'^placementcell/$',placementcell,name='placementcell'),
                re_path(r'^news_events/$',news_events,name='news_events'),
                re_path(r'^news1/(?P<id>[0-9]+)',news1,name='news1'),
                re_path(r'^news2/(?P<id>[0-9]+)',news2,name='news2'),

                # re_path(r'^all_events/$',all_events,name='all_events'),

                


                 re_path(r'^contact/$',contact,name='contact'),
                 re_path(r'^videogallery/$',videogallery,name='videogallery'),
                 re_path(r'^cop_video/$',cop_video,name='cop_video'),

                 re_path(r'^news_letter/$',news_letter,name='news_letter'),
                 re_path(r'^career/$',career,name='career'),
                 re_path(r'^online_appl_portal/$',online_appl_portal,name='online_appl_portal'),
                 re_path(r'^applictionform/$',applictionform,name='applictionform'),
 url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 




]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

