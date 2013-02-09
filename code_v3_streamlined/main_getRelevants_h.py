#!/usr/lib/python3.0

from PARAMETERS import *
from links_group_hash import *
from contingencytable import *
from communityvotecounts import *
from binomial_improved import *
from representativeLink_h import *

f = open(PATH+"/Work/NumComsAndModularities","r")

for line in f:
	elements = line.split()
	DirPath = elements[0]
	numComs = int(elements[1])
#	print DirPath, numComs
	links_group_hash(DirPath)
	contingencytable(DirPath, numComs)
	communityvotecounts(DirPath, numComs)
	binomial(DirPath,numComs)
	representativeLink_h(DirPath,numComs)
f.close()
