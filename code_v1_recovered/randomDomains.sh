Num=300
i=0
while [ $i -lt $Num ]; do
#shuf ../Domains/domain_list.txt | head -10 > ./randomDomains/random$i
shuf randomDomains.txt | head -10 > ./randomDomains/random$i
i=$((i + 1))
done
