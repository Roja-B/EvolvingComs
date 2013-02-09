#!/usr/lib/python3.0

''' This program creates rows of the contingency table of links vs. communities.'''
def contingencytable(dirPATH,M): # dirPATH will be read from NumComsAndModularities
#import sys
#PATH = sys.argv[1]
#dirname = sys.argv[2]
#PATH = PATH+'/'+dirname
#PATH = "./ResultsJaccard30day14slide/"+dirname
#M = int(sys.argv[3])

#PATH = raw_input('Enter data path: ')
#M = int(raw_input('Enter the number of communities: '))
	try:
		f = open(dirPATH+'/links.txt',"r")
     		t = open(dirPATH+'/contingencyTable.txt',"w")
     		w = open(dirPATH+'/linkVoteCounts.txt',"w")
	except:
		print 'error opening file'

	# read all users into a hash table and save their memberships
 	Membership = {}
	for i in range(0,M):
     		try:
        		c = open(dirPATH+'/community'+str(i),"r")
     		except: 
     			print "could not find community"+str(i)
     			continue
     		for line in c:
     			user = line.strip()
     			Membership[user] = i
	print Membership
	# one line in f looks like this: linkid userid1 userid2 ....
	for line in f:
		community = [0]*M
     		link = line.split(' ')[0]
     		users = line.split(' ')
     		users.remove('\n')
      		users.remove(link)
		# count number of votes from each community to this link
     		for user in users:
     			try:
           			memb = int(Membership[user])
             			community[memb] += 1
#				print "user found", user
     			except:
#                   		print "this user was not found in any communities:", user
     	     	    		continue
#     	     if sum(community) == 0: continue  # TODO: why do I have this?
		w.write(str(sum(community))+'\n')
     	     	t.write(link)
     	     	for i in range(0,M):
     	         	t.write('\t'+str(community[i]))
     	     	t.write('\n')
	t.close()
	f.close()
	w.close()
