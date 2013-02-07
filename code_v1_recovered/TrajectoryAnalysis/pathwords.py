# note: wordPathGreen opens WordScores for each community. but this file includes only top 100 words. so it's not good for entropy calculation. but suitable for finding top words
NUMTOP = 100 # specifies how many of the top words in each community to use for aggregation over trajectory
#OPTION = "NoLowVotes"
OPTION = "H_Value"


TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]


for name in TrajectoryNames:
    print name
    f1 = open("Words/"+OPTION+"/wordPath"+name,"r")
    t = open("Words/"+OPTION+"/top"+str(NUMTOP)+"Words"+name+"Path","w")
    for line in f1:
        PATH = line.strip()
        print PATH
	t.write(PATH)
        try: f2 = open(PATH,"r")
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
                print word
        f2.close()
    f1.close()
    t.close()
