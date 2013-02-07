
import sys, math
from collections import defaultdict
PATH = "/media/data3/roja/Balatarin/CompleteRun/PathAnalysis"

#PATH = "./test/RepLinkDomains"
#PATH = "./randomDomains/random"
#M = 3000

colors = ["Red","Black","Blue","Green"]


for color in colors:
	print color
	t = open(PATH+"/WordCounts"+color,"r")
	frequencies = defaultdict(int)
	total = 0.0
	richness = 0.0
	for line in t:
		line = line.strip()
		entity = line.split("\t")[0]
		count = float(line.split("\t")[1])
		frequencies[entity] = count
		total += count
		richness += 1	
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
	print ent, richness/2**ent


