f = open("article_tags.txt", "r")
z = f.readlines()
#tags=""
#for y in z:
#    tags = tags + y

text = ""
f = open("article_text_only.txt", "r")
x = f.readlines()
for y in x:
    text =  text + y

#tags = ["<span style=\"font-size: 10px;\"><span style=\"line-height: 1.714285714;\">Image: PD</span></span>", "<strong>", "</strong>", "<strong>","</strong>","<span style=\"color: #008080;\"><strong>","</strong>","</span>","<span style=\"text-decoration: underline; color: #008080;\">","<a href=\"","\" target=\"_blank\"><span style=\"color: #008080; text-decoration: underline;\">","</span></a></span>","Relevant Reading: <span style=\"text-decoration: underline; color: #008080;\"><a href=\"","\" target=\"_blank\"><span style=\"color: #008080; text-decoration: underline;\">","</span></a></span>","<strong><span style=\"color: #008080;\">","</span>","</strong>", "<span style=\"color: #008080;\"><a href=\"","\"><span style=\"color: #008080;\">", "</span></a>", "<span style=\"font-size: 10px;\">","</span>"]
#need to think about how I am going to deal with the link... I think we are going to have writers put it next to the actual wording of the link then I can pull it out and put in the source code.

#we will likely need to check the first letter of each line before we choose it.
#basically I can do a loop where I count(2 counters, one for x and one for the tags)
# through and depending on the count I can do the next
#thing in a list of items that matches.

both = ""

count=0

for y in z:
    if y.find("//\\") != -1:
        both = both + y + x[count]
        count = count + 1
    else:
        both = both + y + "\n" 
both=both.replace("//","")
both=both.replace("\\","")
print both
'''
for y in x:
    text = text + "<strong>"
    text= text+ x[2][:len(x[2])-1] + "</strong>\n<strong>"
    text= text+ x[4][:len(x[4])-1] + "</strong>\n<strong>"
    text = text + x[6][:len(x[6])-1] + "</strong>\n<span style=\"color: #008080;\"><strong>Study Rundown:</strong> </span>" + x[8][15:]
'''

g = open("try1.txt", "w")
g.write(both)
