from combiner import *
from counter import *
from noPunct import *
from PARAMETERS import *

f = open(PATH+"/Work/NumComsAndModularities","r")

for line in f:
	myPATH = line.split()[0]
	combineWords(myPATH+"/normalizedlinkTexts")
	filename = noPunct(myPATH+"/normalizedlinkTextsCombined")
	wordFreq = wordCounts(filename)
	t = open(myPATH+"/normalizedWordCounts","w")
	for key in wordFreq:
        	t.write(key+"\t"+str(wordFreq[key])+"\n")
	t.close()
f.close()
