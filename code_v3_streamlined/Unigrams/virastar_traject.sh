#!/bin/sh -e
# TODO: parameters are repeated
OPTION=H_Value
MYPATH="/media/data2/roja/Balatarin/CompleteRun2"
DATAPATH="/media/data2/roja/Balatarin/data"

cp virastar.rb $MYPATH/Unigrams/Links/$OPTION/
cd $MYPATH/Unigrams/Links/$OPTION/
filenames=$(ls linkTextsPath*)
for filename in $filenames; do
	echo $filename
	ruby virastar.rb $filename > normalized$filename
done

