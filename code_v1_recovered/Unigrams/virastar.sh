#!/bin/sh -e
dirnames=$(ls /media/data3/roja/Balatarin/CompleteRun/Results)


for dirname in $dirnames; do
	ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community*
	numcoms=$(ls /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/community* |wc -l)
	echo $((numcoms-1))
	number=0
# this line is for the total links per window
#	ruby virastar.rb /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/RelevantLinks/linkTexts >/media/data3/roja/Balatarin/CompleteRun/Results/$dirname/RelevantLinks/normalizedlinkTexts

# this loop is for each community in a window
	while [ $number -lt $((numcoms-1)) ]; do
		ruby virastar.rb /media/data3/roja/Balatarin/CompleteRun/Results/$dirname/RelevantLinks/NoLowlinkTexts$number >/media/data3/roja/Balatarin/CompleteRun/Results/$dirname/RelevantLinks/NoLownormalizedlinkTexts$number
		number=$((number + 1))
	done
done

