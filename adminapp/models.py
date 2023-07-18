from pydoc import describe
from django.db import models

# Create your models here.
class home_wallpaper(models.Model):
    wallpaper_text=models.CharField(max_length=150)
    wallpaper_pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
class news_tbl1(models.Model):
    picture=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    title=models.CharField(max_length=200)
    post_date=models.CharField(max_length=60)
    description=models.TextField()
class news_tbl2(models.Model):
    picture=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    title=models.CharField(max_length=200)
    post_date=models.CharField(max_length=60)
    description=models.TextField()

class photo_gallery(models.Model):
    pictures=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
class notifications(models.Model):
    title=models.CharField(max_length=250)
    post_date=models.CharField(max_length=60)
    description=models.TextField()
    picture=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')

class careers(models.Model):
    pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
class newsletters(models.Model):
    pdf = models.FileField()
    month_year=models.CharField(max_length=150)
class videogallery_link(models.Model):
    youtube_link=models.TextField()
class institution_list(models.Model):
    institution_name=models.CharField(max_length=150)
    institution_picture=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    institution_link=models.CharField(max_length=150)
class appliction_form(models.Model):
    pdf = models.FileField()
    title=models.CharField(max_length=150)
