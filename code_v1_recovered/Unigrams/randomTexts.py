import sys
from counter import *
from noPunct import *

f = open("/media/data3/roja/Balatarin/data/politics_linkTexts")

linkText = dict()
for line in f:
        link_id = line.split("_")[0].strip()
        linkText[link_id] = line
f.close()


#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
#M = int(sys.argv[3]) # number of communities

#PATH = "./test/RepLinkDomains"
#PATH = "./randomDomains/random"
#M = 

f = open("randomVotes5k.txt","r")
t = open("RandomlinkTexts","w")
for line in f:
	line = line.strip()
	linkID = line.split("\t")[1] 
	try: t.write(linkText[linkID])
	except: print linkID
f.close()
t.close()

