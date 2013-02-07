#!/bin/sh -e

# TODO: parameters are repeated
MYPATH="/media/data2/roja/Balatarin/CompleteRun2"
DATAPATH="/media/data2/roja/Balatarin/data"

dirnames=$(ls $MYPATH/Results)


for dirname in $dirnames; do
#	ls $MYPATH/Results/$dirname/community*
	numcoms=$(ls $MYPATH/Results/$dirname/community* |wc -l)
#	echo $((numcoms-2))
	number=0
# this line is for the total links per window
#	ruby virastar.rb $MYPATH/Results/$dirname/linkTexts > $MYPATH/Results/$dirname/normalizedlinkTexts

# this loop is for each community in a window
	while [ $number -lt $((numcoms-2)) ]; do
		ruby virastar.rb $MYPATH/Results/$dirname/RelevantLinks_h/linkTexts$number > $MYPATH/Results/$dirname/RelevantLinks_h/normalizedlinkTexts$number
#		echo $number
		number=$((number + 1))
	done
done

