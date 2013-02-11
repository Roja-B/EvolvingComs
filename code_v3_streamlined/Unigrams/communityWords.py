''' This program takes link Texts for top links in a community and finds work counts for each community. '''

from combiner import *
from counter import *
from noPunct import *
from PARAMETERS import *
f = open(PATH+"/Work/NumComsAndModularities","r")

for line in f:
	L = line.strip().split()
	myPATH = L[0]+"/RelevantLinks_h"
	M = int(L[1])
	for i in range(M):
#		combineWords(myPATH+"/NoLownormalizedlinkTexts"+str(i))
#		filename = noPunct(myPATH+"/NoLownormalizedlinkTexts"+str(i)+"Combined")
#		wordFreq = wordCounts(filename)
#		t = open(myPATH+"/NoLowWordCounts"+str(i),"w"
		combineWords(myPATH+"/linkTexts"+str(i)+"_normalized")
		filename = noPunct(myPATH+"/linkTexts"+str(i)+"_normalizedCombined")
		wordFreq = wordCounts(filename)
		t = open(myPATH+"/WordCounts"+str(i),"w")
		for key in wordFreq:
        		t.write(key+"\t"+str(wordFreq[key])+"\n")
		t.close()

f.close()
