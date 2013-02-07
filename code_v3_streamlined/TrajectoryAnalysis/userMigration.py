import numpy
#names = ["Red","Blue","Black","Green"]
names = ["A","B1","B1prime","B","Bprime","E","Eprime","C0","D2","D2prime","C","D","F"]

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

PATH = "/media/data3/roja/Balatarin/CompleteRun"
tt = open("AverageMigration","w")
for i in range(len(names)):
	name1 = names[i]
	community_files1 = []
	f = open("userPath"+name1,"r")
	for line in f:
		line = line.strip()
		community_files1.append(PATH+'/'+line)
	f.close()
	for j in range(i+1,len(names)):
#	for j in range(len(names)):
		name2 = names[j]
		print name1,name2
		f = open("userPath"+name2,"r")
	        community_files2 = []
	        for line in f:
        	        line = line.strip()
                	community_files2.append(PATH+'/'+line)
        	f.close()

		N = [1,2,3,4,5,6,7,8,9,10]
#		N = [2,4,6,12,18,24]
		for n in N:
			#tt.write(color+"\t"+ str(n/2)+"\t")
			mutuals = []
			t = open("CommonUsers"+name1+"_"+name2+str(n)+"cycles","w")
#			print n/2," months ------------------"
			for k in range(len(community_files1)):
				com_t1 = community_files1[k]
				t1 = com_t1.split("/")[7]
				try:com_t2 = community_files2[k+n]
				except: 
					print "failed"
					break
#				com_t2 = community_files2[k+n]
                                t2 = com_t2.split("/")[7]
				mutual_relative = mutualUsers(com_t1,com_t2)
				mutuals.append(mutual_relative)
				t.write(t1[4:6]+"/"+t1[6:8]+"/"+t1[8:12]+"\t"+t2[4:6]+"/"+t2[6:8]+"/"+t2[8:12]+'\t'+str(mutual_relative)+'\n')
				print k
			try: tt.write(name1+'_'+name2+'\t'+str(n)+'\t'+str(round(sum(mutuals)/len(mutuals),2))+'\t'+str(numpy.std(mutuals))+'\n')
			except: print "Path not long enough. Skipping."
			t.close()
#				print mutual_relative

tt.close()
