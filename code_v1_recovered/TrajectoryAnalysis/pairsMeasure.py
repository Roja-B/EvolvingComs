
import sys, math
from collections import defaultdict
PATH = "/media/data3/roja/Balatarin/CompleteRun/PathAnalysis"

#PATH = "./test/RepLinkDomains"
#PATH = "./randomDomains/random"
#M = 3000

def nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)


t = open(PATH+"/WordCountsAzari","r")
appearances = defaultdict(int)
total = float(0)
for line in t:
	line = line.strip()
	entity = line.split("\t")[0]
	count = float(line.split("\t")[1])
	appearances[entity] = count
	total += count	
t.close()
score = 0 
for domain in appearances:
	if appearances[domain] > 1: score+=nCr(appearances[domain],2)
print nCr(total,2)
print score
print float(score)/float(nCr(total,2))*100
