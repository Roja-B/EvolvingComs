# makes the file paths for word scores for a given "path" or "trajectory"
f = open("blackpath","r")
for line in f:
#	print line
	line = line.strip()
	p1 = line.split("\t")[0]
	com = line.split("\t")[1]
	date = p1+"community"+com
	print date
f.close()

