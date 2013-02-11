#!/bin/sh -e 
#TODO: parameters are repeated
MYPATH="/media/data2/roja/Balatarin/CompleteRun"
DATAPATH="/media/data2/roja/Balatarin/Data"


dirnames=$(ls $MYPATH/Results)
PathName=$MYPATH/Results

for dirname in $dirnames; do
#	ls $MYPATH/Results/$dirname/community*
	numcoms=$(ls $MYPATH/Results/$dirname/community* |wc -l)
#	echo $((numcoms-2))
	python createPaths.py $PathName $dirname $((numcoms-2))
done
