
f = open("ComEvolutions","r")
t = open("Dates","w")
for line in f:
	t.write(line.split('\t')[0]+'\n')
f.close()
t.close()
