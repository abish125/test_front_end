import urllib2
import time

f = open("titles.txt", "r")
titl = f.readlines()

g = open("titles2.txt", "r")
files = g.readlines()

finaltext=""
titles= []
urls = []

for y in range(len(files)):
    h = open(files[y].strip(), "w")
    r=urllib2.urlopen("http://ebling.library.wisc.edu/rss/opml/all.php?category="+titl[y].strip())
    html=r.read()
    h.write(html)
    h.close()

    i = open(files[y].strip(), "r")
    html=i.readlines()
    i.close()

    for c in html:
        loc = c.find("text=")
        while loc != -1:
            titles= titles + [c[loc+6:loc+90]]
            loc = c.find("text=",loc+10)

    for c in html:
        loc2 = c.find("xmlUrl=")
        while loc2 != -1:
            urls=urls+[c[loc2+8:loc2+200]]
            loc2 = c.find("xmlUrl=",loc2+10)

    #removes the first item from the list
    print len(titles)
    print len(urls)

    titles.pop(0)

    for z in range(len(urls)):
        loc = titles[z].find("\"")
        loc2 = urls[z].find("\"")
        finaltext=finaltext + titles[z][0:loc]+"\n" + urls[z][0:loc2] + "\n"
    h = open(files[y].strip(), "w")
    h.write("")
    h.write(finaltext)
    finaltext=""
    titles= []
    urls = []
    h.close()
