#!/usr/lib/python3.0

'''create the table of binomial probability values between links and communities'''

#import sys
#PATH = sys.argv[1]
#dirname = sys.argv[2]
#M = int(sys.argv[3])
#PATH = "Results"
#dirname = "10050126200902252009/RelevantLinks"
#M = 5 
#PATH = PATH+'/'+dirname



from scipy.misc import comb
def B(n, k,p):

#	binomial = round(comb(n,k)*(p**k)*((1-p)**(n-k)), 5)
	binomial = comb(n,k)*(p**k)*((1-p)**(n-k))
#	print "n,k,pi =", `n`,`k`,`p`
#	print "Binomial value =", `binomial`
	return binomial




def binomial(dirPATH,M):
	try:	
		f_pi = open(dirPATH+'/communityVoteCounts.txt',"r")
		o = open(dirPATH+'/contingencyTable.txt',"r")
#		t = open("testBinomian.txt","w")
#		tt = open('testH_value.txt',"w")
		t = open(dirPATH+'/Binomial.txt',"w")
		tt = open(dirPATH+'/H_value.txt',"w")
	except:
		print 'error opening file'

	comVotes = []
	for line in f_pi: # each line has the number of votes cast by one community
		comVotes.append(float(line.strip()))
	f_pi.close()
	#print comVotes
	totalVotes = sum(comVotes)
	Prob = []  # this is the vector of probabilities for binomial distribution for each community
	for i in range(len(comVotes)): Prob.append(comVotes[i]/totalVotes)
#print "community votes=",comVotes[0:10]
#print "total Votes=",totalVotes
#print "pi values=",Prob[0:10]
#print sum(Prob)

	numVotes = dict()
	for line in o:
		linkVotes = 0
		L = line.strip().split("\t")
		linkID = L[0]
#		print L
		for i in range(M):
#			print "L[i+1]=",L[i+1] 
			linkVotes += float(L[i+1])
		numVotes[linkID] = numVotes # this is the vector of link votes
#		print linkVotes
#		if linkVotes == 0: 
#			print "no votes for this link were found", line 
		t.write(linkID)
		tt.write(linkID)
		for i in range(M):	
			observed = int(L[i+1])
#			print "numVotes,observed,Prob[i]=",linkVotes,observed,Prob[i]
#			print "observed, linkVotes, Pi =",observed,linkVotes*Prob[i]
          # we would like to only compute the probability for the case where we have more observed votes than expected number of votes from community i to link  
			if (observed < linkVotes*Prob[i]) or (linkVotes*Prob[i]) == 0: # if prob of a vote is zero, it means the community has cast no votes, in our case it means it has been too small and we have ignored it. if linkVotes is zero, it means it only had votes from low0vote users who were eliminated.
				t.write('\tNA')
				tt.write('\tNA')
#				print "observed votes are below mean: skipping"
			else: 
				binom = B(linkVotes,observed,Prob[i])
				if linkVotes*Prob[i] == 0 : print "problem!"
				H = binom*linkVotes
				t.write('\t'+str(binom))
				tt.write('\t'+str(H))
#				print binom,H
		t.write('\n')
		tt.write('\n')
	f_pi.close()
	o.close()
	t.close()
