
import sys, math
from collections import defaultdict
from PARAMETERS import *
#PATH = "/media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Domains/"
#PATH = "./test/RepLinkDomains"
#PATH = "./randomDomains/random"
#M = 3000


#colors = ["E","Pink","Red","Black","Blue","Green"]
#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

for name in TrajectoryNames:
	print name,"Random"
	t = open(PATH+"/DomainCountsRandom"+name,"r")
	frequencies = defaultdict(int)
	total = float(0)
	for line in t:
		line = line.strip()
		entity = line.split("\t")[0]
		count = float(line.split("\t")[1])
		frequencies[entity] = count
		total += count	
	t.close()

	ent = 0.0
	fSum = total
	probDist = []
	for key in frequencies:
		probDist.append(float(frequencies[key])/fSum)
	for p in probDist:
		ent = ent + p * math.log(p, 2)
	ent = -ent
#       print 'Shannon entropy:'
	print ent


