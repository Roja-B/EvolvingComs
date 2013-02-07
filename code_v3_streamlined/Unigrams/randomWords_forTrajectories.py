from combiner import *
from counter import *
from noPunct import *


PATH = "."
combineWords(PATH+"/RandomlinkTexts")
filename = noPunct(PATH+"/RandomlinkTextsCombined")
wordFreq = wordCounts(filename)
t = open(PATH+"/RandomWordCounts","w")
for key in wordFreq:
        t.write(key+"\t"+str(wordFreq[key])+"\n")
t.close()



#	M = int(L[1])
#	for i in range(M):
#		combineWords(PATH+"/linkTexts"+str(i))
#		filename = noPunct(PATH+"/linkTexts"+str(i)+"Combined")
#		wordFreq = wordCounts(filename)
#		t = open(PATH+"/WordCounts"+str(i),"w")
#		for key in wordFreq:
#        		t.write(key+"\t"+str(wordFreq[key])+"\n")
#		t.close()


