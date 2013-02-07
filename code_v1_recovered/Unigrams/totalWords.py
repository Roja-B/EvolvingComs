from counter import *
from noPunct import *


PATH = "/media/data3/roja/Balatarin/data"
filename = noPunct(PATH+"/politics_linkTextsCombined_normalized")

wordFreq = wordCounts(filename)
t = open("totalWordCounts","w")

for key in wordFreq:
        t.write(key+"\t"+str(wordFreq[key])+"\n")

t.close()

