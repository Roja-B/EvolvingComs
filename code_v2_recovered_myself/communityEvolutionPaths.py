''' this program reads the table of community evolutions (one line per time window) and produces pathways of community evolutions:
	for example: c1-->c0-->c5-->c1-->c1-->c0-->....
each line in the output is the community in the path at time ti and the probability of coming to that community from the previous community in previous line'''
import string,sys
#PATH = sys.argv[1]
#START_TIME =int(sys.argv[2])
PATH = "/media/data2/roja/Balatarin/CompleteRun/W30S14/Results"
START_TIME =int(sys.argv[1])
t = open(PATH+"/EvolutionPaths"+str(START_TIME),"w")
#t = open(PATH+"/Results/EvolutionPathsTopUsers"+str(START_TIME),"w")
def getComSize(_date,com):
	_date = "1005"+_date.replace("-","")
	print _date
	f=open(PATH+"/{0}/communityStats".format(_date),"r") 
#        f=open(PATH+"/Results/{0}/TopUsercommunityStats".format(_date),"r")
	f.readline()
	for line in f:
		line = line.strip()
#		density = line.split(' ')[3]
		size = line.split(' ')[1]  
        	community = line.split(' ')[0] 
		print community,com
		if community == com: 
    			f.close()
			return size
def getNextCom(i,line):
#	print i, line
	nextCom = line.split('\t')[i+1].split('[')[1].split(']')[0]
	prob = line.split('\t')[i+1].split(',')[1]
	return nextCom,prob
f = open(PATH+"/ComEvolutions","r")
#f = open(PATH+"/Results/ComEvolutionsTopUsers","r")
timeStep = 0
while timeStep < START_TIME:
	line1 = f.readline().strip()
	timeStep += 1
lines = f.readlines()
f.close()
for communityPair in line1.split('\t'):
	print communityPair
	if "," not in communityPair :
		date = communityPair
		continue
	print "time step= ",timeStep
	com = communityPair.split(',')[0].split('(')[1]
	print "*********** back to time window ",timeStep, " - Community",com
	t.write("\n *********** Starting at time window "+str(timeStep)+" - Community"+com+'\n')
	#print com
	[com,probability] = getNextCom(int(com),line1)
	for n in range(len(lines)):
		line = lines[n].strip()
		print com, probability
		dates = line.split('\t')[0]
		size = getComSize(dates,com)
		print size
		if size==None : 
                        print "Reached a dead end. (Community too small). stopping..."
                        break
		t.write(dates+"\t"+com+'\t'+probability+'\t'+size+'\n')
		[nextCom,probability] = getNextCom(int(com),line)
		com = nextCom
		try: int(com)
		except: 
			print "there were two available paths. stopping..."
			break
t.close()


