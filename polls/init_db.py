#this is is where you initialize the database
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import RSSFeed, Specialty, Disease, Article
import feedparser
import string
import pyflot
from django.db import models
import datetime
from django.utils import timezone


class RSSFeed(models.Model):
    link = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    impact_number = models.IntegerField()
    additional_info = models.CharField(max_length=2000)
    clinical_vs_bench = models.IntegerField() 
    
class Specialty(models.Model):
    name = models.CharField(max_length=100)
    
class Disease(models.Model):
    name = models.CharField(max_length=200)
    specialty = models.ForeignKey(Specialty)
    mortality = models.IntegerField()
    prevalence = models.IntegerField()
    
class Article(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    specialty = models.ForeignKey(Specialty)
    disease = models.ForeignKey(Disease)
    feed = models.ForeignKey(RSSFeed)

'''
pw=range(11)
pw[0]="http://www.nejm.org/action/showFeed?jc=nejm&type=etoc&feed=rss"
pw[1]="http://www.nature.com/nm/current_issue/rss/"
pw[2]="http://annals.org/rss/site_25/90.xml"
pw[3]="http://journals.lww.com/annalsofsurgery/_layouts/OAKS.Journals/feed.aspx?FeedType=CurrentIssue"
pw[4]="http://archsurg.jamanetwork.com/rssfeeds.aspx"
pw[5]="http://www.annemergmed.com/current.rss"
pw[6]="http://www.ajconline.org/current.rss"
pw[7]="http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1097-0142"
pw[8]="http://www.plosmedicine.org/article/feed"
pw[9]="http://www.cmaj.ca/rss/current.xml"
pw[10]="http://pediatrics.aappublications.org/rss/current.xml"
c_cardio=0
feeds=[]

r = RSSFeed(link="http://www.nejm.org/action/showFeed?jc=nejm&type=etoc&feed=rss", name="NEJM",impact_number="1", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://www.nature.com/nm/current_issue/rss/", name="Nature",impact_number="1", additional_info="", clinical_vs_bench="2")
r = RSSFeed(link="http://annals.org/rss/site_25/90.xml", name="Annals of Medicine", impact_number="3", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://journals.lww.com/annalsofsurgery/_layouts/OAKS.Journals/feed.aspx?FeedType=CurrentIssue", name="Annals of Surgery", impact_number="3", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://archsurg.jamanetwork.com/rssfeeds.aspx", name="JAMA", impact_number="1", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://www.annemergmed.com/current.rss", name="Annals of Emergency Medicine", impact_number="4", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://www.ajconline.org/current.rss", name="AJC", impact_number="4", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://onlinelibrary.wiley.com/rss/journal/10.1002/(ISSN)1097-0142", name="Wiley", impact_number="5", additional_info="", clinical_vs_bench="2")
r = RSSFeed(link="http://www.plosmedicine.org/article/feed", name="PLOS Medicine", impact_number="5", additional_info="", clinical_vs_bench="1")
r = RSSFeed(link="http://www.cmaj.ca/rss/current.xml", name="CMAJ", impact_number="5", additional_info="", clinical_vs_bench="2")
r = RSSFeed(link="http://pediatrics.aappublications.org/rss/current.xml", name="Pediatrics", impact_number="3", additional_info="", clinical_vs_bench="1")
'''


#code works to fill the database with all the articles
#few warnings: /home/abish125/ENV/lib/python2.6/site-packages/django/db/models/fields/__init__.py:808: RuntimeWarning: DateTimeField received a naive datetime (2012-11-01 15:05:12) while time zone support is active. RuntimeWarning)
 
feeds = []
titles = []
pw=range(1,12)
for p in pw:
    r=RSSFeed.objects.get(id=p)
    feeds=feedparser.parse(r.link)
    for item in feeds["items"]:
    	a = Article(title=item["title"],date=datetime.datetime(*item.updated_parsed[:6]), feed=r)
    	a.save()

    	
#Now need to put the titles in the database (for now make the disease, specialty blank.) later i can edit it with
#p.choice_set.create(choice_text='The sky', votes=0)
#how do i know which feed it came from? might need to use the above code

class Article(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    specialty = models.ForeignKey(Specialty)
    disease = models.ForeignKey(Disease)
    feed = models.ForeignKey(RSSFeed)



print titles
    
#After I do that I can make a loop that updates the new titles in the Article database

#After that you can put in the disease and specialty with p.choice_set.create(choice_text='The sky', votes=0)
feeds = []
titles = []
pw=range(1,12)
for p in pw:
    fp = feedparser.parse(p)
    for item in fp["items"]:
    		feeds = feeds + [item["title"]]
    		if item["title"].lower().find("cardiovascular") != -1:
        		c_cardio = c_cardio + 1
        		
        		
f= open('/home/abish125/ENV/mysite/polls/list_of_diseases.txt', 'r')
x= f.readlines()
y= x[0].split('\r')

for z in y:
     d=Disease(name=z)
     d.save()
     for article in Article.objects.all():
     	if article.title.lower().find(article.title) != -1:
     		article.disease=d
     		article.save()
     	
d = Disease.	
for article in Disease.article_set.all():
     print article.name
     


# Make sure our __unicode__() addition worked.
>>> Poll.objects.all()
[<Poll: What's up?>]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Poll.objects.filter(id=1)
[<Poll: What's up?>]
>>> Poll.objects.filter(question__startswith='What')
[<Poll: What's up?>]

# Get the poll whose year is 2012.
>>> Poll.objects.get(pub_date__year=2012)
<Poll: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Poll.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Poll matching query does not exist. Lookup parameters were {'id': 2}

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Poll.objects.get(id=1).
>>> Poll.objects.get(pk=1)
<Poll: What's up?>

# Make sure our custom method worked.
>>> p = Poll.objects.get(pk=1)
>>> p.was_published_recently()
True

# Give the Poll a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.
>>> p = Poll.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> p.choice_set.all()
[]

# Create three choices.
>>> p.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> p.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = p.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Poll objects.
>>> c.poll
<Poll: What's up?>

# And vice versa: Poll objects get access to Choice objects.
>>> p.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> p.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any poll whose pub_date is in 2012.
>>> Choice.objects.filter(poll__pub_date__year=2012)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = p.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
