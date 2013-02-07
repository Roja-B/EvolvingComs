#!/usr/bin/python
# -*- coding: utf-8 -*-

# This program compares two lists of word counts and writes a score for each word

import operator
f1 = open("totalWordCounts","r")
stopwords = open("stopwordList").read()
totalCount = dict()

maxTotal = 0
while True:
	line = f1.readline()
	line = line.strip()
	try: countTotal = int(line.split("\t")[1])
	except: break
        word = line.split("\t")[0].strip()
        if word in stopwords: continue # this ensures we are not counting stop words in the total corpus
	if countTotal > maxTotal : maxTotal = countTotal
	totalCount[word] = countTotal
f1.close()
print "Number of uque non-stopword words in the whole corpus = ", len(totalCount)

pathfile = open("PATHS","r")
for p in pathfile:
        PATH = p.strip()
	f2 = open(PATH+"/RelevantLinks/WordCounts","r")
	f2.readline()
	wordCount = dict()
	maxCount = 0
	while True:
		line = f2.readline()
		line = line.strip()
	        try:count = int(line.split("\t")[1])
		except: break
                word = line.split("\t")[0].strip()
                if word in stopwords: continue
		if count>maxCount: maxCount = count
		wordCount[word] = count
	f2.close()

	score = dict()
	for word in wordCount:
		if wordCount[word] == 1: continue
		w1 = float(wordCount[word])/float(maxCount)
		w2 = float(totalCount[word])/float(maxTotal)
		wordScore = round(w1-w2,5) 
		score[word] = wordScore
		#except: 
#			print word
		#	continue
#        t = open("testWordScores","w")
	print PATH
	t = open(PATH+"/RelevantLinks/WordScores","w")
	sorted_x = sorted(score.iteritems(), key=operator.itemgetter(1),reverse=True)
	for pair in sorted_x[1:100]:
#		print pair[0].decode("utf-8")
		t.write(pair[0]+"\t"+str(pair[1])+'\n')
	t.close()
	

