NUM_LINKS = 351801
#NUM_LINKS = 10
def combineWords(filename):
	t = open(filename+"Combined","w")
	f = open(filename,"r")
	for i in range(NUM_LINKS):
		line = f.readline().strip()
#		print line
#		if len(line.split("_")) > 2 : print len(line.split("_"))
		linkID = line.split("_")[0]
		line = line.replace(linkID+"_","\n")
		t.write(line + " ")
	t.close()
	f.close()

#PATH = "/media/data3/roja/Balatarin/data"
#combineWords(PATH+"/politics_linkTexts")                                              
