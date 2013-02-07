
t = open("blackpath","w")
f = open("domainPathBlack","r")
for line in f:
	line = line.strip()
	p = line.split("RelevantLinks/RepLinkDomains")
	t.write(p[0]+'\t'+p[1]+'\n')

t.close()
f.close()
