from combiner import *
from counter import *
from noPunct import *

f = open("PATHS","r")

for line in f:
	PATH = line.strip()+"/RelevantLinks"
	combineWords(PATH+"/normalizedlinkTexts")
	filename = noPunct(PATH+"/normalizedlinkTextsCombined")
	wordFreq = wordCounts(filename)
	t = open(PATH+"/normalizedWordCounts","w")
	for key in wordFreq:
        	t.write(key+"\t"+str(wordFreq[key])+"\n")
	t.close()
f.close()
