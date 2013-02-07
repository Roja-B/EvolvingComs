from combiner import *
from counter import *
from noPunct import *

f = open("PATHSplusCOMS","r")

for line in f:
	L = line.strip().split("\t")
	PATH = L[0]+"/RelevantLinks/RelevantLinks_h"
	M = int(L[1])
	for i in range(M):
#		combineWords(PATH+"/NoLownormalizedlinkTexts"+str(i))
#		filename = noPunct(PATH+"/NoLownormalizedlinkTexts"+str(i)+"Combined")
#		wordFreq = wordCounts(filename)
#		t = open(PATH+"/NoLowWordCounts"+str(i),"w")
               combineWords(PATH+"/linkTexts"+str(i))
               filename = noPunct(PATH+"/normalizedlinkTexts"+str(i)+"Combined")
               wordFreq = wordCounts(filename)
               t = open(PATH+"/WordCounts"+str(i),"w")

		for key in wordFreq:
        		t.write(key+"\t"+str(wordFreq[key])+"\n")
		t.close()

f.close()
