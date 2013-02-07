# makes the file paths for word scores for a given "path" or "trajectory"

from PARAMETERS import *

#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
#TrajectoryNames = ["11","12","21","22"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

#OPTION = "NoLowVotes"
OPTION = "H_Value"

for name in TrajectoryNames:
	print "Path ",name
	f = open("Path"+name,"r")
	t = open("Domains/domainPath"+name,"w")
	#f.readline()
	for line in f:
		line = line.strip()
		date = line.split("\t")[0]
		date = date.replace("-","")
#		print line.split("       ")
		try: com = line.split("\t")[1]
		except: 
			print line
			break
		#date = "Results/1005"+date+"/RelevantLinks/RepLinkDomainVotes"+com
		if OPTION == "NoLowVotes": date = PATH+"/Results/1005"+date+"/RelevantLinks/NoLowLinkDomains"+com
		elif OPTION == "H_Value" : date = PATH+"/Results/1005"+date+"/RelevantLinks_h/LinkDomains"+com
		t.write(date+'\n')
#		print date

	f.close()
	t.close()

