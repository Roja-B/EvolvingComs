
def noLow(PATH):
	try:f = open(PATH+"/contingencyTable.txt","r")
	except: print PATH
	linkvotes = dict()
	for line in f:
        	line = line.strip()
	        linkID = line.split("\t")[0]
	       	line = string.replace(line, linkID,"").strip()
        	numvotes = 0
        	for element in line.split("\t"): numvotes += int(element)
        	linkvotes[linkID] = numvotes
	f.close()

