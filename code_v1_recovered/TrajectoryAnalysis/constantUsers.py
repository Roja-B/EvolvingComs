# This program aggregates users in each trajectory and compares user membership for every pair of trajectories. 

import numpy
TrajectoryNames = ["A","B1","B1prime","B","Bprime","E","Eprime","C0","D2","D2prime","C","D","F"]

PATH = "/media/data3/roja/Balatarin/CompleteRun/W30S14"
TrajectoryUsers = dict()
for i in range(len(TrajectoryNames)):
	name = TrajectoryNames[i]
	# read the path to the file containing users in each community in a trajectory, the file paths are saved in userPath... 
	f = open("userPath"+name,"r")
	intersectUsers = set()
	firstSetFlag = 1
	for line in f:
		line = line.strip()
		ff = open(PATH+'/'+line,"r")
		comUsers = set()
		for line_ff in ff:
			userID = line_ff.strip()
	                comUsers.add(userID)
		if firstSetFlag:
			firstSetFlag = 0 
			intersectUsers = comUsers
		else: intersectUsers = set.intersection(intersectUsers,comUsers)
		ff.close()
	print name, len(intersectUsers)
	f.close()



