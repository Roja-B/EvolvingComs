
# Parameters:
CHUNK = 6
#Time = 27
#Time = 40
Time = 54
GAP = 18
ELECTION = 73
PATH ="/media/data3/roja/Balatarin/CompleteRun/W30S14"

print "chunk size = ", CHUNK
print "Time start = ", Time
print "Gap = ", GAP
# "Dates" file is a product of this code: makeDates.py
f = open("Dates","r")

# save sets of users active in each time window in an array
activeUsers = dict()
cycle = 1
cycleMap = dict()
for line in f:
	date = line.strip()
	cycleMap[date] = cycle
	filename = PATH+"/Results/1005"+date.replace("-","")+"/AllUsers"
	f1 = open(filename,"r")
	users = set()
	for line in f1:
		users.add(line.strip())
	activeUsers[cycle] = users
	f1.close()
	cycle += 1
f.close()
MAXDATE = len(activeUsers)

TrajectoryNames = ["A","B1","B1prime","Bprime","E","Eprime"]

for TRAJECTORY in TrajectoryNames:
	# save sets of users active in each trajectory at each time window
	comUsers = dict()
	f = open("TrajectoryAnalysis/Path"+TRAJECTORY,"r")
	for line in f:
		line = line.strip()
		date = line.split("\t")[0]
		cycle = cycleMap[date]
		try: com = line.split("\t")[1]
		except: 
			print line
			break
		filename = "/Results/1005"+date.replace("-","")+"/community"+com
		f1 = open(PATH+filename,"r")
		users = set()
		for line in f1:
			users.add(line.strip())
		comUsers[cycle] = users
		f1.close()
	f.close()

	trajStart = min(comUsers.keys())
	print "------------------------"
#	print "Trajectory begins at cycle", trajStart
	print TRAJECTORY
	# Find users active in a "CHUNK" of the trajectory
	trajectoryChunk = set()
	allUsersChunk = set()
	for cycle in range(Time,Time+CHUNK+1):
#	for cycle in range(trajStart,trajStart+CHUNK+1):
		try: trajectoryChunk = set.union(trajectoryChunk,comUsers[cycle])
		except: 
			print "Range does not apply to this trajectory"
			break
		allUsersChunk = set.union(allUsersChunk, activeUsers[cycle])
		print "cycle = ", cycle
	if len(trajectoryChunk)==0: continue
	# Find all users active a "CHUNK" a year later
	LATER = Time + GAP
	allUsersLater = set()
#	for t in range(ELECTION,ELECTION+CHUNK+1):
	for t in range(LATER,LATER+CHUNK+1):
		allUsersLater = set.union(allUsersLater,activeUsers[t])
		print "t = ",t
	dropped = trajectoryChunk - allUsersLater
#	print len(dropped),len(trajectoryChunk)
	print "Trajectory Drop= ", float(len(dropped))/float(len(trajectoryChunk))
	allUserDrop = allUsersChunk - allUsersLater
	print "Total Drop= ", float(len(allUserDrop))/float(len(allUsersChunk))
	print len(allUserDrop)
	print len(allUsersChunk)
	print "Percent deviation from total= " , 100*(float(len(dropped))/float(len(trajectoryChunk)) - float(len(allUserDrop))/float(len(allUsersChunk)))

