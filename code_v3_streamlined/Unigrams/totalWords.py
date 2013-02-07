''' This program finds total word counts in politics links'''
from counter import *
from noPunct import *
from PARAMETERS import *

#PATH = "/media/data3/roja/Balatarin/data"
filename = noPunct(DATAPATH+"/politics_linkTextsCombined_normalized")

wordFreq = wordCounts(filename)
t = open("totalWordCounts","w")

for key in wordFreq:
        t.write(key+"\t"+str(wordFreq[key])+"\n")

t.close()

