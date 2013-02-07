#!/bin/sh -e
dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results)


for dirname in $dirnames; do
	ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community*
	numcoms=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	PathName=/media/data3/roja/Balatarin/CompleteRun/Results
	python createPaths.py $PathName $dirname $((numcoms-1))
done
