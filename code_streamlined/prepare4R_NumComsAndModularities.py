
from PARAMETERS import *
#PATH = "/media/data2/roja/Balatarin/CompleteRun"
f = open(PATH+"/Work/NumComsAndModularities","r")
t = open(PATH+"/Work/NumComsAndModularities_betterformat","w")
for line in f:
        line = line.strip()
#       if "/" not in line:
#               t.write(line+'\n')
#               continue
        numComs = line.split(" ")[1]
        dates = line.split(" ")[0].split("/")[7]
        modularity = line.split(" ")[2]
	k = len(str(prefix))
        t.write(dates[k:k+8]+"-"+dates[k+8:len(dates)]+"\t"+numComs+'\t'+modularity+'\n')
        # was like this 10051019200911182009
	# now like this: 100101200701312007
f.close()
t.close()


