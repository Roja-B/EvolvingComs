#this program aggregates all linkIDs over one trajectory
NUMTOP = 50 # number of top links to read
TrajectoryNames = ["A","B","Bprime","B1","B1prime","E","Eprime","C","C0","D2","D2prime","D","F"]

for name in TrajectoryNames:
    f1 = open("Links/H_Value/linkPath"+name,"r")
    t = open("Links/H_Value/Links"+name+"Path","w")
    for line in f1:
        PATH = line.strip()
        print PATH
#	t.write(PATH)
        try: f2 = open("../"+PATH,"r")
        except: 
            print "could not open",PATH
            continue
        for i in range(NUMTOP):
                L = f2.readline()
                L = L.strip()
                try:linkID = L.split(" ")[1]
		except: 
			print line
			continue
                t.write(linkID+'\n')
                #print linkID
        f2.close()
    f1.close()
    t.close()
