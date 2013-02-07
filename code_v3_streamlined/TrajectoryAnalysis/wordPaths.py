# makes the file paths for word scores for a given "path" or "trajectory"
# the number of top words to consider from each community is only considered in the previous creation of NoLowWordScores by computeWordScoresPerCommunity.py


from PARAMETERS import *
#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
#TrajectoryNames = ["1","2","11","12","21","22"] 
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

#PATH = "/media/data3/roja/Balatarin/CompleteRun"
#OPTION = "NoLowVotes"
OPTION = "H_Value"

for name in TrajectoryNames:
	print "Path", name
	f = open("Path"+name,"r")
	t = open("Words/wordPath"+name,"w")
	for line in f:
	#	print line
		line = line.strip()
		date = line.split("\t")[0]
		date = date.replace("-","")
		try: com = line.split("\t")[1]
		except: 
			print line
			continue
		if OPTION =="NoLowVotes" : date = PATH+"/Results/"+prefix+date+"/RelevantLinks_h/NoLowWordScores"+com
		elif OPTION =="H_Value": date = PATH+"/Results/"+prefix+date+"/RelevantLinks_h/WordScores"+com
		t.write(date+'\n')
#		print date
	f.close()
	t.close()

