# note: wordPathGreen opens WordScores for each community. but this file includes only top 100 words. so it's not good for entropy calculation. but suitable for finding top words

# Parameters
from PARAMETERS import *
NUMTOP = 10  # the number of top links to consider from each community

#TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]
#TrajectoryNames = ["11","12","21","22"]
TrajectoryNames = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

#OPTION = "NoLowVotes"
OPTION = "H_Value"


for name in TrajectoryNames:
    f1 = open("Domains/domainPath"+name,"r")
    t = open("Domains/Domains"+name+"Path","w")
    for line in f1:
        myPATH = line.strip()
        #print myPATH
	t.write(myPATH+'\n')
        try: f2 = open(myPATH,"r")
        except: 
            print "could not open",myPATH
            continue
	for i in range(NUMTOP):
                L = f2.readline()
                L = L.strip()
                domain = L.split(" ")[0]
                t.write(domain+'\n')
#                print domain
        f2.close()
    f1.close()
    t.close()
