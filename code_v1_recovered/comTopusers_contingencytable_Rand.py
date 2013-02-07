#!/usr/lib/python3.0
# Another version of com_contingency_Rand.py which only considers top users in each community, as provide in files TopUserCommunity
''' This program creates rows of the contingency table for the adjusted rand index between two communities, as well as matrices of transition probabilities between communities at different times, and the rand index over time.

The sorted timeline (also names of directories) of graphs is in U-pol_J100VT5_stats_combined.txt, the number of communities in each is in NumComsAndModularities_betterformat '''

import sys
import string
import math
def intersect(a,b):
        return list(set(a) & set(b))

def union(a,b):
        return list(set(a) | set(b))

PATH = sys.argv[1]
prefix = "100"

# creates contingency table between two consecutive time windows given by dirname1 and dirname2. Requires the number of communities detected in each time window as paranemeters numCom1 and numCom2
def contingency(dirname1,dirname2,numComs1,numComs2):
	PATH1 = PATH + '/Results/' + dirname1
	PATH2 = PATH + '/Results/' + dirname2
	filename = PATH+'/Results/TopUserComContingencyTable'+dirname1+'.txt'
	t = open(filename,"w")
	# add one row and one column for users that are only in one of the two communities
	Cluster1 = [set() for i in range(numComs1+1)]
	Cluster2 = [set() for i in range(numComs2+1)]
	X1 = set()
	X2 = set()

	# read usernames 
	for i in range(numComs1):
		try: f = open(PATH1+'/topuser_community'+str(i),"r")
		except: 
			print PATH1,'/topuser_community',str(i)," does not exist (community too small)."
			continue
		for line in f:
			userID = line.strip()
			Cluster1[i].add(userID)
		X1 = X1 | Cluster1[i] 
		f.close()
	
	for i in range(numComs2):
       		try: f = open(PATH2+'/topuser_community'+str(i),"r")
                except:
                        print PATH2,'/topuser_community',str(i)," does not exist (community too small)."
                        continue

	        for line in f:
        	        userID = line.strip()
                	Cluster2[i].add(userID)
		X2 = X2 | Cluster2[i]
		f.close()

	Cluster1[numComs1] = X2-X1
	Cluster2[numComs2] = X1-X2
	for i in range(numComs1+1):
		for j in range(numComs2+1):
			index = len(intersect(Cluster1[i],Cluster2[j]))
			t.write(str(index)+'\t')
		t.write('\n')
	print len(X1-X2)
	print len(X2-X1)
	t.close()
	return filename

def rand(date,contingencyfilename):
	f = open(contingencyfilename,"r")
	a = []
	b = []
	n = []
	i = 0
	for line in f:
		line = line.strip()
		n.append([])
		n[i] = line.split("\t") 
		i += 1

	M1 = len(n) # no. of communities in clustering1
	M2 = len(n[0]) # no. of communities in clustering2

	index = 0 
	for i in range(M1):
		a.append(0)	
		for j in range(M2):
			element = int(n[i][j])
			index += element*(element-1)/2  # this is n choose 2 
			a[i] += int(n[i][j])
	for j in range(M2):
		b.append(0)
		for i in range(M1):
			b[j] += int(n[i][j])

#print a
#print b

	N = sum(a)
        print "N=",N
	if N==1:return
	sum_a = 0
	sum_b = 0
	for i in range(M1): sum_a += a[i]*(a[i]-1)/2
	for j in range(M2): sum_b += b[j]*(b[j]-1)/2

	expectedIndex = float(sum_a*sum_b)/(N*(N-1)/2)
	maxIndex = 1/2.0*(sum_a+sum_b)
	if (maxIndex == expectedIndex): 
		return 
	adjusted_Rand = (index - expectedIndex)/(maxIndex - expectedIndex)

	t = open(PATH+"/Work/RandIndecesOverTime_TopUsers.txt","a")
	t.write(date+'\t'+str(adjusted_Rand)+'\n')
	t.close()

def transitionProb(date,contingencyfilename):
	f = open(contingencyfilename,"r")
	n_t1 = []
	n_t2 = []
	n = []
	i = 0
	for line in f:
       		line = line.strip()
	        n.append([])
        	n[i] = line.split("\t")
        	i += 1

	M1 = len(n) # no. of communities in clustering1
	M2 = len(n[0]) # no. of communities in clustering2

	sum_all = 0
	for i in range(M1):
	        n_t1.append(0)
	        for j in range(M2):
                	sum_all += int(n[i][j])
        	        n_t1[i] += int(n[i][j])
	
	for j in range(M2):
        	n_t2.append(0)
	        for i in range(M1):
        	        n_t2[j] += int(n[i][j])

#print n_t1
#print n_t2

	N = sum(n_t1)
	print "N=",N
	p = []
	for i in range(M1):
        	p.append([])
        	if n_t1[i] == 0 : 
			for j in range(M2):
				p[i].append(0)
			continue
	        for j in range(M2):
        	        p_t1 = float(n_t1[i])/N
	                p_t2 = float(n_t2[j])/N
                	joint_p = float(n[i][j])/sum_all
        	        p[i].append(round(joint_p/p_t1,3))
	
	print p

        t = open(PATH+"/Results/TrProbsTopUsers"+date,"w")
	for i in range(M1):
		for j in range(M2):
        		t.write(str(p[i][j])+'\t')
		t.write('\n')
        t.close()


#----------- main() ---------------
graphDates = []
f = open(PATH+"/Work/U-pol_J100VT_stats.txt","r")
#f = open(PATH+"/Work/U-pol_L-VT5_stats.txt","r")
for line in f:
        graphDate = line.split(" ")[0]
        numNodes = int(line.split(" ")[1])
        if numNodes <= 3 :continue # this is because com-finding fails for a graph with 3 nodes or less
        graphDates.append(graphDate)
f.close()

# Question: why are we reading from two different files?!
# answer: because we really want the information in NumComs, but the dates are not in order
graphs = dict()
f = open(PATH+"/Work/NumComsAndModularities_betterformat","r")
for line in f:
        graphDate = line.split("\t")[0]
        numComs = line.split("\t")[1]
        graphs[graphDate] = numComs
f.close()

for i in range(len(graphDates)-1):
	date1 = graphDates[i]
	date2 = graphDates[i+1]
	dirname1 = prefix+string.replace(date1,"-","")
        dirname2 = prefix+string.replace(date2,"-","")

#	print date1, date2

	try:num1 = int(graphs[graphDates[i]])
	except:
		print "window did not produce communities:", graphDates[i]
		continue

	try:num2 = int(graphs[graphDates[i+1]])
	except:
                print "window did not produce communities:", graphDates[i+1]
                continue
#	print num1,num2 
	contingencyfilename = contingency(dirname1,dirname2,num1,num2)
	rand(date1,contingencyfilename)
	transitionProb(date1,contingencyfilename)

