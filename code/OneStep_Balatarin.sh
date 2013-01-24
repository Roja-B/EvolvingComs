#!/bin/bash -e

# ---- define and save parameters
MAX_INDEX=1534
VOTE_THRESHOLD=10
WINDOW_SIZE=60
SLIDE_AMOUNT=30
MYPATH="/media/data2/roja/Balatarin/CompleteRun2"
DATAPATH="/media/data2/roja/Balatarin/data"

# ----- don't change anything below this point
PREFIX=$VOTE_THRESHOLD
rm PARAMETERS.py;
echo "VOTE_THRESHOLD = "$VOTE_THRESHOLD >> PARAMETERS.py
echo "WINDOW_SIZE = "$WINDOW_SIZE >> PARAMETERS.py
echo "SLIDE_AMOUNT = "$SLIDE_AMOUNT >> PARAMETERS.py
echo "PATH = "\"$MYPATH\" >> PARAMETERS.py
echo "DATAPATH = "\"$DATAPATH\" >> PARAMETERS.py
echo "prefix = "\"$PREFIX\" >> PARAMETERS.py
mkdir W$WINDOW_SIZE\S$SLIDE_AMOUNT\T$VOTE_THRESHOLD

# ---- create bipartite graphs
mkdir $MYPATH/bipartite
# bipartite.sh: 
index=0
while [ $index -le $MAX_INDEX ]
do
  python extract_bipartite_pro.py $index $WINDOW_SIZE 
  index=$(( $index + $SLIDE_AMOUNT ))
  echo $index 
done

# ---- create unipartite graphs
mkdir $MYPATH/unipartite
# unipartite.sh
index=0
while [ $index -le $MAX_INDEX ]
do
  python makeUnipartiteGraph_pro.py $index $WINDOW_SIZE 
  index=$(( $index + SLIDE_AMOUNT ))
  echo $index
done

# ---- detect communities and save in Results directory
mkdir $MYPATH/Results
mkdir $MYPATH/Work
mv $MYPATH/unipartite/*stats.txt $MYPATH/Work 
# TODO: in the file "prepare4R_NumComsAndModularities.py" used in this script there is a problem with thre prefix assuming it will only take the space before this: [4:12]. this must be corrected 

#detectcommunities.sh
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


# ---- produce contingency tables between communities at different times and find transition probabilities and evolution paths
#./paths.sh

# ---- create edgelist of community evolution graph and visualize
#python createComEvolutionNetwork.py 
#python getComSizes_temp.py
#python layered_balatarin.py


