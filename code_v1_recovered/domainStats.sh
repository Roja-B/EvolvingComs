#!/bin/bash

dirnames=$(ls Results/)
for dirname in $dirnames; do
	numcoms=$(ls Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	PathName=Results
	python domainVotes.py $PathName $dirname $((numcoms-1))
	mv $PathName/$dirname/domainVotes.txt $PathName/$dirname/RelevantLinks
done
