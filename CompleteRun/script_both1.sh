#!/bin/bash
#index=0
#window=60
#end=1534
##mkdir /media/data3/allen/bipartite/W30S7T
#while [ $index -le $end ]
#do
#  python extract_bipartite_pro.py $index $window #W30S7T
#  index=$(( $index + 30 ))
#  echo $index 
#done

index=0
window=30
end=1534
while [ $index -le $end ]
do
  python makeUnipartiteGraph_pro.py $index $window W30S14T2
  index=$(( $index + 14 ))
  echo $index
done


#mkdir /media/data3/allen/unipartite/W30S7T
#while [ $index -le $end ]
#  python makeUnipartiteGraph_pro.py $index $window W30S7T
#  index=$(( $index + 14 ))
#  echo $index
#done
