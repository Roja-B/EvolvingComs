#!/bin/bash

dirnames=$(ls Results/)
for dirname in $dirnames; do
        numcoms=$(ls Results/$dirname/community* |wc -l)
        echo $((numcoms-1))
        PathName=Results
        python findLinkDomains.py $PathName $dirname/RelevantLinks $((numcoms-1))

done
