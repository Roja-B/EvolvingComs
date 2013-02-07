import numpy
from PARAMETERS import *

#colors = ["Red","Blue","Black","Green"]
#colors = ["Mixed"]
#colors = ["A","B","Bprime","B1","B1prime","C","C0","D","D2","D2prime","E","Eprime","F"]
colors = ["A","B","Bprime","B1prime","E","Eprime","C","D1","D1prime","D2","D2prime","D","F","Small"]

# this function returns percentage of users in filename1 who are in filename2
def mutualUsers(filename1,filename2):
	f1 = open(filename1,"r")
	f2 = open(filename2,"r")
	com1Users=set()
	com2Users=set()
	for line in f1:
		userID = line.strip()
		com1Users.add(userID)
	for line in f2:
        	userID = line.strip()
        	com2Users.add(userID)
	f1.close()
	f2.close()
#	return(float(len(set.intersection(com1Users,com2Users)))/float(len(set.union(com1Users,com2Users))))
        return(float(len(set.intersection(com1Users,com2Users)))/float(len(com1Users)))
#        return(float(len(set.intersection(com1Users,com2Users)))/float(len(com2Users)))

#PATH = "/media/data3/roja/Balatarin/CompleteRun"
tt = open("AverageCommonUsers","w")
for color in colors:

	community_files = []
	f = open("userPath"+color,"r")
	for line in f:
		line = line.strip()
		community_files.append(PATH+'/'+line)
	f.close()
#	N = [1,2,3]
	#N = [2,3,4,5,6,12,18,24]
	N = [2,3,4,5,6,7,8,10,12,14,16,18,20,22,24]
	for n in N:
		#tt.write(color+"\t"+ str(n/2)+"\t")
		mutuals = []
		t = open("CommonUsers"+color+"_"+str(n)+"cycles","w")
#		print n/2," months ------------------"
		for i in range(len(community_files)):
			com_t1 = community_files[i]
			t1 = com_t1.split("/")[7]
			try:com_t2 = community_files[i+n]
			except: break
			mutual_relative = mutualUsers(com_t1,com_t2)
			mutuals.append(mutual_relative)
			t.write(t1[4:6]+"/"+t1[6:8]+"/"+t1[8:12]+"\t"+str(mutual_relative)+'\n')
		try: tt.write(color+'\t'+str(n)+'\t'+str(round(sum(mutuals)/len(mutuals),2))+'\t'+str(numpy.std(mutuals))+'\n')
		except: print "Path not long enough. Skipping."
		t.close()
tt.close()

