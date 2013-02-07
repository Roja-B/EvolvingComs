
MAXCOUNT = 1000
def wordCounts(filename):
	f = open(filename,"r")
	wordCount = dict()
	totalCount = 0
	for line in f:
		line = line.strip()
		# tokenize
		tokens = line.split(" ")
		# populate the dictionary
		for word in tokens:
			totalCount += 1
			try:  wordCount[word] +=1
			except KeyError: wordCount[word]=1
			#if word in wordCount: wordCount[word] +=1 
			#else: wordCount[word]=1
		print totalCount
		#if totalCount > MAXCOUNT: 
		#	f.close()
		#	return wordCount
	f.close()
	return wordCount

#PATH = "/media/data3/roja/Balatarin/data"
#wordFreq = wordCounts(PATH+"/politics_linkTextsCombined")
#t = open("testWordCounts","w")

#for key in wordFreq:
#	t.write(key+"\t"+str(wordFreq[key])+"\n")

#t.close()

