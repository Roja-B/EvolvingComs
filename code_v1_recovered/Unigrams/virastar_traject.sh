#!/bin/sh -e
OPTION=H_Value
cp virastar.rb /media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/$OPTION/
cd /media/data3/roja/Balatarin/CompleteRun/TrajectoryAnalysis/Links/$OPTION/
filenames=$(ls linkTextsPath*)
for filename in $filenames; do
	echo $filename
	ruby virastar.rb $filename > normalized$filename
done

