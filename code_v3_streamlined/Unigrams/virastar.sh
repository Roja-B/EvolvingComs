#!/bin/sh 

# TODO: parameters are repeated
MYPATH="/media/data2/roja/Balatarin/CompleteRun"
DATAPATH="/media/data2/roja/Balatarin/data"

dirnames=$(ls $MYPATH/Results)


for dirname in $dirnames; do
#	ls $MYPATH/Results/$dirname/community*
#	numcoms=$(ls $MYPATH/Results/$dirname/community* |wc -l)
#	echo $((numcoms-2))
#	number=0
# this line is for the total links per window
#	ruby virastar.rb $MYPATH/Results/$dirname/linkTexts > $MYPATH/Results/$dirname/normalizedlinkTexts

# this loop is for each community in a window
	filenames=$(ls $MYPATH/Results/$dirname/RelevantLinks_h/linkTexts*)
#	#while [ $number -lt $((numcoms-2)) ]; do
	for filename in $filenames; do
		#ruby virastar.rb $MYPATH/Results/$dirname/RelevantLinks_h/linkTexts$number > $MYPATH/Results/$dirname/RelevantLinks_h/normalizedlinkTexts$number
		ruby virastar.rb $filename > $filename\_normalized 
		echo $filename
#		echo $number
#		number=$((number + 1))
	done
done

