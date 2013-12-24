# Create your views here.
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import RSSFeed, Specialty, Disease, Article, DOI
import feedparser
import string

def index(request):

    context = Context({
            'feeds': "hello",
            'graph': "world",
            'c_cardio': "my name",
            })
    return render(request, 'polls/login.html', context)

from django.shortcuts import render

def search_results(request):
    if 'q' in request.GET and request.GET['q']:
        q =request.GET['q']
        doi = DOI.objects.filter(doi__icontains=q)
        return render(request, 'polls/search_results.html',
                      {'doi': doi, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def search_form(request):
    return render(request, 'polls/search_form.html')

def claim(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        n = request.GET['name']
        r = request.GET['role']
        doi = DOI.objects.filter(doi__icontains=q)
        if doi.__len__()==0:
            d = DOI(doi=q, name=n, role=r)
            d.save()
        return render(request, 'polls/claim.html',
                      {'doi': doi, 'query': q, 'name': n, 'role': r})
    else:
        return HttpResponse('Please submit a search term.')
    return render(request, 'polls/claim.html')

def submit_article(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        doi = DOI.objects.filter(doi__icontains=q)
        l_ids = []
        if doi.__len__()!=0:
            for d in doi:
                l_ids = l_ids + [d.id]
            d = DOI.objects.filter(id = max(l_ids))
            return render(request, 'polls/submit_article.html',
                          {'name':q, 'doi':d[0]})


def smart(request):
    return render(request, 'polls/smart.html')
    
def smart2(request):
    t=request.GET['1']
    return render(request, 'polls/convert_text2.html',{'text':t})

def convert_text(request):
    return render(request, 'polls/convert_text.html')

def convert_text2(request):
    f = open("/home/abish125/ENV/mysite/polls/article_tags.txt", "r")
    z = f.readlines()

    text = ""
    f = ""
    x = f
    for y in x:
        text =  text + y

    t=[]
    x = range(16)
    for y in x:
	t=t+[request.GET[str(y+1)]]

    t=t+["hello"]+["hello"]+["hello"]

    #tags = ["<span style=\"font-size: 10px;\"><span style=\"line-height: 1.714285714;\">Image: PD</span></span>", "<strong>", "</strong>", "<strong>","</strong>","<span style=\"color: #008080;\"><strong>","</strong>","</span>","<span style=\"text-decoration: underline; color: #008080;\">","<a href=\"","\" target=\"_blank\"><span style=\"color: #008080; text-decoration: underline;\">","</span></a></span>","Relevant Reading: <span style=\"text-decoration: underline; color: #008080;\"><a href=\"","\" target=\"_blank\"><span style=\"color: #008080; text-decoration: underline;\">","</span></a></span>","<strong><span style=\"color: #008080;\">","</span>","</strong>", "<span style=\"color: #008080;\"><a href=\"","\"><span style=\"color: #008080;\">", "</span></a>", "<span style=\"font-size: 10px;\">","</span>"]
    #need to think about how I am going to deal with the link... I think we are going to have writers put it next to the actual wording of the link then I can pull it out and put in the source code.

    #we will likely need to check the first letter of each line before we choose it.
    #basically I can do a loop where I count(2 counters, one for x and one for the tags)
    # through and depending on the count I can do the next
    #thing in a list of items that matches.

    both = []

    count=0

    for y in z:
        if y.find("//\\") != -1:
             both = both + [y + t[count] + "\n"]
             count = count + 1
        else:
             both = both + [y + "\n"]
             
    newboth=[]
    for b in both:
        b=b.replace("//","")
        b=b.replace("\\","")
        newboth = newboth + [b]

    '''
    for y in x:
        text = text + "<strong>"
        text= text+ x[2][:len(x[2])-1] + "</strong>\n<strong>"
        text= text+ x[4][:len(x[4])-1] + "</strong>\n<strong>"
        text = text + x[6][:len(x[6])-1] + "</strong>\n<span style=\"color: #008080;\"><strong>Study Rundown:</strong> </span>" + x[8][15:]
    '''

    return render(request, 'polls/convert_text2.html',
               {'text':newboth})



'''
def rs_import():
    pw="http://www.nejm.org/action/showFeed?jc=nejm&type=etoc&feed=rss"
    feed = feedparser.parse(pw)	

    for item in feed["items"]:
    	if item["title"].lower().find("cardiovascular") != -1:
       	     print item["title"]
       	     
'''       	     
       	 	
