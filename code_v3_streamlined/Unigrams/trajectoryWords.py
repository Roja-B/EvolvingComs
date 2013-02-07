from combiner import *
from counter import *
from noPunct import *

OPTION = "H_Value"
#OPTION = "NoLowVotes"

TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/"+OPTION

for name in TrajectoryNames:
	combineWords(PATH+"/normalizedlinkTextsPath"+name)
	filename = noPunct(PATH+"/normalizedlinkTextsPath"+name+"Combined")
	wordFreq = wordCounts(filename)
	t = open(PATH+"/WordCountsPath"+name,"w")
	for key in wordFreq:
        	t.write(key+"\t"+str(wordFreq[key])+"\n")
	t.close()





