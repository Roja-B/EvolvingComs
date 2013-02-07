#!/bin/bash

python prepare4R_NumComsAndModularities.py 
rm Work/RandIndecesOverTime_withUnsharedNodes.txt
python com_contingencytable_Rand.py
mkdir Results/ComContingencyTable100
mkdir Results/TransitionProbs
mv Results/ComContingencyTable* Results/ComContingencyTable100/
mv Results/TrProbs* Results/TransitionProbs/
cp createplots.R Work
cd Work
R --save < createplots.R
cd ..


