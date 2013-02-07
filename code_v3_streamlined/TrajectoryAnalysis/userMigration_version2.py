PATH = "/media/data3/roja/Balatarin/CompleteRun/"
TrajectoryNames = ["A","B1","B1prime","Bprime","E","Eprime","C0","D2","D2prime","C","D","F"]

# This function returns percentage of users in filename1 who are in filename2
def mutualUsers(filename1,filename2):
	f1 = open(filename1,"r")
	f2 = open(filename2,"r")
	com1Users=set()
	com2Users=set()
	for line in f1:
		userID = line.strip()
		com1Users.add(userID)
	for line in f2:
        	userID = line.strip()
        	com2Users.add(userID)
	f1.close()
	f2.close()
#        return(float(len(set.intersection(com1Users,com2Users)))/float(len(com1Users)))
        return(float(len(set.intersection(com1Users,com2Users))**2)/float(len(com1Users))*len(com2Users))
# Read dates from file into a dict
f = open("Dates","r")
Dates = dict() 
DateIndex = dict()
t = 1
for line in f:
	date = line.strip()
	Dates[t] = date
	DateIndex[date] = t
	t += 1 
f.close()
#print Dates
MAXDATE = max(Dates)


# Get the start and finish dates
startTime = dict()
finishTime = dict()

for Traj in TrajectoryNames:
	f1 = open("Path"+Traj,"r")
	startTime[Traj] = DateIndex[f1.readline().split('\t')[0]]
	for line in f1: continue 
	finishTime[Traj] = DateIndex[line.split('\t')[0]]
	f1.close()

TrajectoryPaths = dict()
for Traj in TrajectoryNames:
	paths = dict()
	startTime[Traj]
	f1 = open("userPath"+Traj,"r")
	i = 0
	for line in f1:
		line = line.strip()
		paths[startTime[Traj]+i] = line 
		i += 1
	TrajectoryPaths[Traj] = paths
	f1.close()
#print TrajectoryPaths

tt = open("AverageMigrationV2_squared","w")
for Tr1 in TrajectoryNames:
	for Tr2 in TrajectoryNames:
		print Tr1,Tr2
		# Find min and max delta_t to be used between two Trajectories
		maxDelta_t = min(finishTime[Tr1]-startTime[Tr1],finishTime[Tr2]-startTime[Tr1])
		#minDelta_t = max(1,finishTime[Tr1]-startTime[Tr2])
		minDelta_t = max(1,startTime[Tr2]-finishTime[Tr1])
		for Delta_t in range(minDelta_t,maxDelta_t):
			print Delta_t
			mutuals = []
			for t in range(startTime[Tr1],finishTime[Tr1]):
				if t+Delta_t > MAXDATE : break
				com_t1 = TrajectoryPaths[Tr1][t] 
				try: com_t2 = TrajectoryPaths[Tr2][t+Delta_t]
				except: 
#					print "Trajectory 2 ended or has not started yet?"
					continue
				mutual_relative = mutualUsers(PATH+com_t1,PATH+com_t2)
				mutuals.append(mutual_relative)
			if len(mutuals)== 0: continue
			average = sum(mutuals)/len(mutuals)
			tt.write(Tr1+'\t'+Tr2+'\t'+str(Delta_t)+'\t'+str(round(average,3))+'\n')

tt.close()








