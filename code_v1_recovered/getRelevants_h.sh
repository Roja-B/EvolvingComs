#!/bin/bash 

dirnames=$(ls Results/)
#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
#dirnames=$(ls ./test)
for dirname in $dirnames; do

	numcoms=$(ls Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	PathName=Results
	python binomial.py $PathName $dirname/RelevantLinks $((numcoms-1))
	mkdir $PathName/$dirname/RelevantLinks/RelevantLinks_h
	mv $PathName/$dirname/RelevantLinks/Binomial.txt $PathName/$dirname/RelevantLinks/RelevantLinks_h
	mv $PathName/$dirname/RelevantLinks/H_value.txt $PathName/$dirname/RelevantLinks/RelevantLinks_h
	python representativeLink_h.py $PathName $dirname/RelevantLinks/RelevantLinks_h $((numcoms-1))
#	python makeLinkURL.py $PathName $dirname $((numcoms-1))
	python findLinkDomain.v2.py $PathName $dirname $((numcoms-1))

done
