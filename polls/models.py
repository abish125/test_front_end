from django.db import models
from django.contrib.auth.models import User
import datetime

class RSSFeed(models.Model):
    link = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    impact_number = models.IntegerField()
    additional_info = models.CharField(max_length=2000)
    clinical_vs_bench = models.IntegerField() 
    
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    
class Disease(models.Model):
    specialty = models.ForeignKey(Specialty)
    name = models.CharField(max_length=200)
    mortality = models.IntegerField()
    prevalence = models.IntegerField()
    
class Article(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    specialty = models.ForeignKey(Specialty)
    disease = models.ForeignKey(Disease)
    feed = models.ForeignKey(RSSFeed)

class DOI(models.Model):
    doi = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    role = models.CharField(max_length=50)

class Note(models.Model):
    uid = models.ForeignKey(User)
    time_created = models.DateTimeField('time created')
    title = models.CharField(max_length=1000)
    content_text = models.CharField(max_length=10000)
    
    #content_signal = models.ForeignKey(    
    #Note(1,1,"1986-12-05 12:12" ,'hello', "this is a note")  This worked after i made a user a = User(1, "andrew")

