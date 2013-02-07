import operator
from PARAMETERS import *
#OPTION = "NoLowVotes"
OPTION = "H_Value"


def wordCounts(filename):
	f = open(filename,"r")
	wordCount = dict()
	for line in f:
		line = line.strip()
		if line.split("/")[0] == "Results": continue		
		# populate the dictionary
		word = line			
		if word in wordCount: wordCount[word] +=1 
		else: wordCount[word]=1
	f.close()
	return wordCount

#PATH = "/media/data3/roja/Balatarin/data"
#wordFreq = wordCounts(PATH+"/politics_linkTextsCombined")
#for key in wordFreq:
#	t.write(key+"\t"+str(wordFreq[key])+"\n")
#t.close()

myPATH = PATH+"/TrajectoryAnalysis"

#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
#TrajectoryNames = ["11","12","21","22"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

for name in TrajectoryNames:

#	wordFreq = wordCounts(myPATH+"/Domain/DomainsRandom"+name)
	wordFreq = wordCounts(myPATH+"/Domains/Domains"+name+"Path")

#	t = open("Domains/DomainCountsRandom"+name,"w")
	t = open(myPATH+"/Domains/DomainCounts"+name,"w")

	sorted_x = sorted(wordFreq.iteritems(), key=operator.itemgetter(1),reverse=True)

	for pair in sorted_x:
#		print pair
		t.write(pair[0]+'\t'+str(pair[1])+'\n')
	t.close()

