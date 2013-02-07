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
#M = 3000

pathfile = open("PATHSplusCOMS","r")
for p in pathfile:
	L = p.strip().split("\t")
	PATH = L[0]
	M = int(L[1])
	for i in range(M):
                f = open(PATH+"/RelevantLinks/NoLowTop50Links"+str(i))
		#f = open(PATH+"/RelevantLinks/top10Links"+str(i))
		t = open(PATH+"/RelevantLinks/NoLowlinkTexts"+str(i),"w")
		for line in f:
			line = line.strip()
			linkID = line.split(" ")[1] 
			chi2 = float(line.split(" ")[2])
			if chi2<= 0.0:continue
			t.write(linkText[linkID])
		f.close()
		t.close()

	



#filename = noPunct(PATH+"/RelevantLinks/linkTexts")

#wordFreq = wordCounts(filename)
#t = open(PATH+"/RelevantLinks/WordCounts","w")

#for key in wordFreq:
#        t.write(key+"\t"+str(wordFreq[key])+"\n")

#t.close()

