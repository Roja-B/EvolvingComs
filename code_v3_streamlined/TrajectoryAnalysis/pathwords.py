# note: wordPathGreen opens WordScores for each community. but this file includes only top 100 words. so it's not good for entropy calculation. but suitable for finding top words
NUMTOP = 100 # specifies how many of the top words in each community to use for aggregation over trajectory
#OPTION = "NoLowVotes"
OPTION = "H_Value"

#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
#TrajectoryNames = ["1","2","11","12","21","22"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]
 
for name in TrajectoryNames:
    print "Path ",name
    f1 = open("Words/wordPath"+name,"r")
    t = open("Words/top"+str(NUMTOP)+"Words"+name+"Path","w")
    for line in f1:
        myPATH = line.strip()
 #       print PATH
	t.write(myPATH)
        try: f2 = open(myPATH,"r")
        except: 
		print line
		continue
#        while True: # read all the words in each community
	for i in range(NUMTOP):
                L = f2.readline()
		if L == "\n": break
                L = L.strip()
                word = L.split("\t")[0]
		if word == "": break 
		t.write(word+'\n')
#                print word
        f2.close()
    f1.close()
    t.close()
