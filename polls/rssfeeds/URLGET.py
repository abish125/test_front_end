import urllib2
r=urllib2.urlopen("http://ebling.library.wisc.edu/rss/")
text=r.read()

#these are commands used below (useful for what you need)
#print text.lower().find("showRSS".lower())
#print text.lower().find("showRSS".lower(), 13074)
#+10 then the next few
#print text[13223:13254]

prevloc = 0
loc = text.lower().find("showrss")
ss = ""
title = ""
titles = ""
start=0
prevchar=""
while loc != -1:
    ss = text[loc+5:loc+110]
    for x in ss:
        if x == "'" and start == 0 and prevchar !="\\":
            start = 1
            continue
        elif x == "'" and start != 0 and prevchar !="\\":
            break
        elif start != 0 and x == " ":
            title = title + "_"
        elif start != 0 and x != "\\":
            title = title + x
        prevchar = x
    title = title + ".txt"
    title = title.lower()
    print title
    titles = titles + title + '\n'
    title= ""
    prevloc=loc+10
    loc=text.lower().find("showrss",prevloc)
    start = 0

f= open("titles2.txt", "w")
f.write(titles)

