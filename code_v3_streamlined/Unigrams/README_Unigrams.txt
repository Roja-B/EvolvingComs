1) run ./paths_to_files.sh to create a list of all paths for time windows

to get the total counts:
run python totalWords.py


to get the counts per window:
1) run python windowTexts.py (to extract the text for each window)
2) run python windowWords.py (to get the word counts)
3) run python computeWordScores.py 

to get the counts per community:
1) run python top100LinksPerCom.py (to get a list of top 100 links for each community)
2) run python communityTexts.py    (to get the text of the top 100 links per community)
3) run python communityWords.py    (to get the word counts)
4) run python computeWordScoresPerCommunity.py

to get the counts for a random list of links:
1) run python randomTexts.py (to get the text of randomly generated links)
2) run ./splitRandomLinks.sh (to split the random texts into sets of 10)
3) run python randomWords.py (to count words for each set)
-----------------------------------

In order to repeat using the persian text virastar.rb: 

to get the total counts:
1) run virastar.rb on the data, politicsTexts_Combined
2) run python totalWords.py

to get the counts per window: (These are all TODOs)
1) run python windowTexts.py (to extract the text for each window)
2) run ./virastar.sh (to change linkTexts to normalizedlinkTexts)
3) run python windowWords.py (to get the word counts)
??3) run python computeWordScores.py

to get the counts per community: (this is only for top 10 links per com - will need to increase this)
1)run python communityTexts.py    (to get the text of the top 10 links per community)
2) run ./virastar.sh (to change NoLowlinkTexts0 to NoLownormalizedlinkTexts0 for each community)
3) run python communityWords.py    (to get the word counts)
4) run python computeWordScoresPerCommunity.py
# this option below only makes sense if we combine links over a trajectory first
4) run python computeWordScoresPerCommunity_compareWtotal.py

------------------
in order to perform these over whole trajectories:

1) run python trajectoryTexts.py
2) run ./virastar_trajec.sh 
3) run python trajectoryWords.py
4) run python computeWordScoresPerTrajectory_compareWtotal.py

---------------------------------

For unigram analysis:
1-get counts per window:
	a.windowTexts.py
	b.windowWords.py
2-get counts per community
	a.communityTexts.py
	b../virastar.sh
	c.communityWords.py
3-assign scores
	a.computeWordScoresPerCommunity.py


