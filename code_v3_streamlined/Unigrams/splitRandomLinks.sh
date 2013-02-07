Num=160
i=0
while [ $i -lt $Num ]; do
#shuf ../Domains/domain_list.txt | head -10 > ./randomDomains/random$i
n=$(((i+1)*10))
head -$n RandomlinkTexts | tail -10 > ./Random/random$i
i=$((i + 1))
done

