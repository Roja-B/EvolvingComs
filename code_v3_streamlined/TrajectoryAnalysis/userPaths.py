# makes the file paths for word scores for a given "path" or "trajectory"
from PARAMETERS import *

#TrajectoryNames = ["E","Pink","B1","B1prime","F","C0","D2","D2prime","Eprime"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]


for name in TrajectoryNames:
	print name
	f = open("Path"+name,"r")
	t = open("userPath"+name,"w")
	for line in f:
		line = line.strip()
		date = line.split("\t")[0]
		date = date.replace("-","")
		try: com = line.split("\t")[1]
		except: 
			print line
			break
		date = "Results/"+prefix+date+"/community"+com
		t.write(date+'\n')
	f.close()
	t.close()
