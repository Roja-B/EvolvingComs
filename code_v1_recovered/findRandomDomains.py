
from findLinkDomainGeneral import *
f1 = open("randomDomains/randomVotes.txt","r")

i = 0
t = open("randomDomains/random"+str(i),"w")
for line in f1:
	i+=1
	if i%10 == 0:
		t.close()
		t = open("randomDomains/random"+str(i/10),"w")
	line = line.strip()
	linkID = line.split("\t")[1]
	try: d = domains[linkID]
	except: continue
	t.write(d+'\n')

f1.close()
t.close()
