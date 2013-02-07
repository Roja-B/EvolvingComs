#!/bin/bash -e

dirnames=$(ls Results/)
#dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/)
for dirname in $dirnames; do
	numcoms=$(ls Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	PathName=Results
	python excludeLowLinks.py $PathName $dirname $((numcoms-1)) 
done
