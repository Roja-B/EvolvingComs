
''' This program reads the ids of top "MAXLINKS" links for each community and writes the [summary] Texts of those links (found from politics_linkTexts)'''
import sys
from counter import *
from noPunct import *
from PARAMETERS import *
MAXLINKS = 50
f = open(DATAPATH+"/politics_linkTexts")

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

pathfile = open(PATH+"/Work/NumComsAndModularities","r")
for p in pathfile:
	L = p.strip().split()
	myPATH = L[0]
	M = int(L[1])
	for i in range(M):
                f = open(myPATH+"/RelevantLinks_h/topLinks"+str(i),"r") # topLinks
		#f = open(myPATH+"/RelevantLinks/top10Links"+str(i))
		t = open(myPATH+"/RelevantLinks_h/linkTexts"+str(i),"w")
		k = 0
		for line in f:
			line = line.strip()
			linkID = line.split(" ")[1] 
		#	chi2 = float(line.split(" ")[2])
		#	if chi2<= 0.0:continue
			t.write(linkText[linkID])
			k += 1
			if k >= MAXLINKS : break
		f.close()
		t.close()

	



#filename = noPunct(PATH+"/RelevantLinks/linkTexts")

#wordFreq = wordCounts(filename)
#t = open(PATH+"/RelevantLinks/WordCounts","w")

#for key in wordFreq:
#        t.write(key+"\t"+str(wordFreq[key])+"\n")

#t.close()

