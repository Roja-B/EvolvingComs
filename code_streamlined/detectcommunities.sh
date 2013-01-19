#!/bin/bash
MAX_INDEX=1534
VOTE_THRESHOLD=10
WINDOW_SIZE=60
SLIDE_AMOUNT=30
MYPATH="/media/data2/roja/Balatarin/CompleteRun2"
DATAPATH="/media/data2/roja/Balatarin/data"

#bfilenames=$(ls /media/data2/roja/Balatarin/CompleteRun/bipartite/)
#ufilenames=$(ls /media/data2/roja/Balatarin/CompleteRun/unipartite/)
bfilenames=$(ls $MYPATH/bipartite/)
ufilenames=$(ls $MYPATH/unipartite/)

for filename in $ufilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]")
        mkdir $MYPATH/Results/$dirname
        cp $MYPATH/unipartite/$filename $MYPATH/Results/$dirname/unipartite.txt
	cp $MYPATH/PARAMETERS.py $MYPATH/Results/$dirname/PARAMETERS
done
for filename in $bfilenames; do
        #dirname=1005$(echo $filename | tr -dc "[:digit:]")  
        dirname=$PREFIX$(echo $filename | tr -dc "[:digit:]")
        echo $dirname
        cp $MYPATH/bipartite/$filename $MYPATH/Results/$dirname/bipartite.txt
done
dnames=$(ls $MYPATH/Results/)
for dname in $dnames; do
        echo $dname
        cp *.R $MYPATH/Results/$dname/
        cd $MYPATH/Results/$dname/
        R --save < main_balatarin.R
	rm PARAMETERS
        cd ../..
done
mv $MYPATH/Results/NumComsAndModularities $MYPATH/Work

