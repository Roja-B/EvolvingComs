colors = ["Random","Red","Black","Blue","Green"]

for color in colors:
	filename ="WordCounts"+color
	f = open(filename,"r")

	count = 0
	for line in f:
		line = line.strip()
		count += int(line.split("\t")[1])
	
	print color,count
	f.close()
