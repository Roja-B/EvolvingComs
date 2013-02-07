# makes the file paths for word scores for a given "path" or "trajectory"
NUMTOP = 50
TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]


for name in TrajectoryNames:
	print name
	f = open("Path"+name,"r")
	t = open("Links/H_Value/linkPath"+name,"w")
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
		date = "Results/1005"+date+"/RelevantLinks/RelevantLinks_h/topLinks"+com
		t.write(date+'\n')
		print date
	f.close()
	t.close()

