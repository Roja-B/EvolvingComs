# makes the file paths for word scores for a given "path" or "trajectory"
TrajectoryNames = ["A","B1","B1prime","Bprime","E","Eprime","C0","D2","D2prime","C","D","F"]


for name in TrajectoryNames:
	print name
	f = open("Path"+name,"r")
	t = open("userPath_top"+name,"w")
	for line in f:
		line = line.strip()
		date = line.split("\t")[0]
		date = date.replace("-","")
		try: com = line.split("\t")[1]
		except: 
			print line
			break
		date = "Results/1005"+date+"/topuser_community"+com
		t.write(date+'\n')
	f.close()
	t.close()
