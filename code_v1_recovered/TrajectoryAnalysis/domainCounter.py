import operator

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

PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis"


TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]

for name in TrajectoryNames:

#	wordFreq = wordCounts(PATH+"/Domains/"+OPTION+"/DomainsRandom"+name)
	wordFreq = wordCounts(PATH+"/Domains/"+OPTION+"/Domains"+name+"Path")

#	t = open("Domains/"+OPTION+"/DomainCountsRandom"+name,"w")
	t = open("Domains/"+OPTION+"/DomainCounts"+name,"w")

	sorted_x = sorted(wordFreq.iteritems(), key=operator.itemgetter(1),reverse=True)

	for pair in sorted_x:
		print pair
		t.write(pair[0]+'\t'+str(pair[1])+'\n')
	t.close()

