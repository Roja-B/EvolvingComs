# This program aggregates users in each trajectory and compares user membership for every pair of trajectories. 

import numpy
TrajectoryNames = ["A","B1","B1prime","B","Bprime","E","Eprime","C0","D2","D2prime","C","D","F"]

PATH = "/media/data3/roja/Balatarin/CompleteRun"
TrajectoryUsers = dict()
for i in range(len(TrajectoryNames)):
	name = TrajectoryNames[i]
	# read the path to the file containing users in each community in a trajectory, the file paths are saved in userPath... 
	f = open("userPath_top"+name,"r")
	trUsers = set()
	for line1 in f:
		line1 = line1.strip()
		ff = open(PATH+'/'+line1,"r")
		for line2 in ff:
			userID = line2.strip()
	                trUsers.add(userID)
	TrajectoryUsers[name] = trUsers
	f.close()
for Tr1 in TrajectoryNames:
	print Tr1,len(TrajectoryUsers[Tr1])

for Tr1 in TrajectoryNames:
	for Tr2 in TrajectoryNames:
#		if Tr1 == Tr2: continue
	        # below are three options for what to return. Uncomment whichever is desired.
#		similarity = float(len(set.intersection(TrajectoryUsers[Tr1],TrajectoryUsers[Tr2])))/float(len(set.union(TrajectoryUsers[Tr1],TrajectoryUsers[Tr2])))
#		similarity = float(len(set.intersection(TrajectoryUsers[Tr1],TrajectoryUsers[Tr2])))/float(len(TrajectoryUsers[Tr1]))
		similarity = float(len(set.intersection(TrajectoryUsers[Tr1],TrajectoryUsers[Tr2]))**2)/float(len(TrajectoryUsers[Tr1])*len(TrajectoryUsers[Tr2]))# this is from van alstyne 2005
		print Tr1, Tr2, similarity

