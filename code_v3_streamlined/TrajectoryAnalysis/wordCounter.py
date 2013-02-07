
NUMTOP = 100
import operator
from PARAMETERS import *

def wordCounts(filename):
	f = open(filename,"r")
	wordCount = dict()
	lineCount = 0
	for line in f:
		line = line.strip()
		if line.split("/")[0] == "Results": continue
		if "/" in line: continue	
		# populate the dictionary
		word = line			
		if word in wordCount: wordCount[word] +=1 
		else: wordCount[word]=1
		lineCount +=1
#		if lineCount > THRESHOLD: break
	f.close()
	return wordCount

#PATH = "/media/data3/roja/Balatarin/data"
#wordFreq = wordCounts(PATH+"/politics_linkTextsCombined")

#for key in wordFreq:
#	t.write(key+"\t"+str(wordFreq[key])+"\n")

#t.close()

#PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Words/NoLowVotes"
#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]

#TrajectoryNames = ["1","2","11","12","21","22"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

for name in TrajectoryNames:
	wordFreq = wordCounts(PATH+"/TrajectoryAnalysis/Words/top"+str(NUMTOP)+"Words"+name+"Path")
	t = open(PATH+"/TrajectoryAnalysis/Words/top"+str(NUMTOP)+"WordCounts"+name,"w")
	sorted_x = sorted(wordFreq.iteritems(), key=operator.itemgetter(1),reverse=True)
	for pair in sorted_x:
	#for key in wordFreq:
		t.write(pair[0]+'\t'+str(pair[1])+'\n')
	       #t.write(key+"\t"+str(wordFreq[key])+"\n")
	t.close()

