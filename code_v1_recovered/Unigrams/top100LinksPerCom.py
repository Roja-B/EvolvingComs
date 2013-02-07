import operator
import sys
from noLow import *
# this program produces the list of top 100 links per community based on the Chi-squared table for each time window

#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
#tablefilename = raw_input("Enter file name: ")

pathfile = open("PATHSplusCOMS","r")
tablefilename = "Chi2.txt"

for line in pathfile:
	line = line.strip()
	L =  line.split("\t")
	PATH = L[0]+"/RelevantLinks"
	M = int(L[1])

	f = open(PATH+'/'+tablefilename,"r")

	Communities= []
	#for each community we need a hash table
	for i in range(M):
		Communities.append(dict())

	for line in f:
	    	link = line.split('\t')[0]
   		for i in range(0,M):
        		count = float(line.split('\t')[i+1])
        		Communities[i][link] = count

	for i in range(0,M):
    		sorted_com = sorted(Communities[i].iteritems(), key=operator.itemgetter(1),reverse=True)
    		t = open(PATH+"/NoLowtop50Links"+str(i),"w")
		length = len(sorted_com)
		count = 0
 	   	for j in range(length)):
			if linkvotes[sorted_com[j][0]] < 10 : continue
			t.write("link "+sorted_com[j][0]+' '+str(sorted_com[j][1])+'\n')
			count +=1
			if count == 50: break
		t.close()
	f.close()


pathfile.close()

