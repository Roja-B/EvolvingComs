#!/bin/bash 
MAX_INDEX=1534
VOTE_THRESHOLD=10
WINDOW_SIZE=60
SLIDE_AMOUNT=30
MYPATH="/media/data2/roja/Balatarin/CompleteRun2"
DATAPATH="/media/data2/roja/Balatarin/data"

python prepare4R_NumComsAndModularities.py
##rm Work/RandIndecesOverTime_withUnsharedNodes.txt
python com_contingencytable_Rand.py
mkdir $MYPATH/Results/ComContingencyTable
mkdir $MYPATH/Results/TransitionProbs
mv $MYPATH/Results/ComContingencyTable* Results/ComContingencyTable/
mv $MYPATH/Results/ComContingencyTable* Results/ComContingencyTable/
mv $MYPATH/Results/TrProbs* Results/TransitionProbs/
#cp createplots.R Work
#cd Work
#R --save < createplots.R
#cd ..

# This is for creating the paths
python communityEvolution.py
i=1
Num=40
while [ $i -lt $Num ]; do
        python communityEvolutionPaths.py $i
#       python CommunityTopicBalatarin.py $i 
        i=$((i + 5))
        echo $i
done
## python communityEvolutionPathsTopics.py to get a list of topics for each community on the path of community evolutions


