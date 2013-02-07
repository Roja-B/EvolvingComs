#!/bin/bash

Num=90
i=5
while [ $i -lt $Num ]; do
        python communityEvolutionPaths.py $i
#       python CommunityTopicBalatarin.py $i 
        i=$((i + 5))
        echo $i
done


