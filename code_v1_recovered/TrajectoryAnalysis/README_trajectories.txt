

python linkPaths.py (this creates file paths)
output --> linkPathC
python linkdomains.py (this aggregates all linkIDs along a trajectory)
output --> LinksCPath

python domainPaths.py  (this creates the file paths) 
output --> domainPathBlue  
python pathdomains.py  (this extracts the domains in a trajectory) 
output --> DomainsBluePath  

python wordPaths.py 
output --> wordPathBlue
python pathwords.py 
output --> WordsBluePath
 NOTE: words are under the Links directory now


python userPaths.py 
output --> usersPathBlue
python userRetention.py

modify, then
run domainCounter.py
run wordCounter.py


run pairsMeasure.py 
or:
run Entropies_Domains.py 
