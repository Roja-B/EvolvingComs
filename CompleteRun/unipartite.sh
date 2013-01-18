#!/bin/bash
index=0
while [ $index -le $MAX_INDEX ]
do
  python makeUnipartiteGraph_pro.py $index $WINDOW_SIZE 
  index=$(( $index + SLIDE_AMOUNT ))
  echo $index
done


