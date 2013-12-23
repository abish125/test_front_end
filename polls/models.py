from django.db import models

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
    
