import urllib2

f = open("biology.txt","r")
html=f.readlines()

titles= []
urls = []

for c in html:
    loc = c.find("text=")
    while loc != -1:
        titles= titles+ [c[loc+6:loc+90]]
        loc = c.find("text=",loc+10)

for c in html:
    loc2 = c.find("xmlUrl=")
    while loc2 != -1:
        urls=urls+[c[loc2+8:loc2+200]]
        loc2 = c.find("xmlUrl=",loc2+10)

#removes the first item from the list
titles.pop(0)

for z in range(len(titles)):
    loc = titles[z].find("\"")
    loc2 = urls[z].find("\"")
    print titles[z][0:loc]
    print urls[z][0:loc2]


#need to ignore the first one.
#now all you need are the urls for the rss feed and you're done



'''
count=0
for x in html[5]:

    print count
    count = count +1
    print x
'''
