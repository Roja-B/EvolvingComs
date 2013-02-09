
#import sys
#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
#M = int(sys.argv[3])
from PARAMETERS import *
f = open(PATH+"/Work/NumComsAndModularities","r")
# Read all directory names and number of communities into a dictionary
numcoms = dict()
for line in f:
	line = line.strip()
	dirname = line.split()[0]
	M = line.split()[1]
	numcoms[dirname] = int(M)
f.close()


# Create a dictionary of linkIds and domains
f1 = open(DATAPATH+"/id_domains.txt","r")
Domains = dict()
for line in f1:
	parsed = line.strip().split(" ")
	try:
		link = parsed[0]
		domain = parsed[1]
		Domains[link] = domain
	except: print line
f1.close()

# Iterate through the directories and extract domains
for dirname in numcoms.keys():
#	dirPATH = PATH+'/Results/'+dirname
	dirPATH = dirname
	for com in range(numcoms[dirname]):
		filename = "%(dirPATH)s/RelevantLinks_h/topLinks%(com)s" %locals()
		try: f2 = open(filename,"r")
		except: 
			print "No such file: ",filename
			continue
		filename = "%(dirPATH)s/RelevantLinks_h/LinkDomains%(com)s" %locals()
		t = open(filename,"w")
		for line in f2:
			linkId = line.strip().split(" ")[1]
			t.write(Domains[linkId]+'\n')
		f2.close()
		t.close()



