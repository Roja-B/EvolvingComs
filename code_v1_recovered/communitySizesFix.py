'''this program was written to correct a bug in some of the data, (in communityStats file). this is now fixed in the original code that produces that file, so it's unnecessary for more recently generated data '''

PATH = "/media/data3/roja/Balatarin/CompleteRun/Results"
f=open(PATH+"/U-pol_J100VT5_stats.txt","r")
dates=[]
for line in f:
    dates.append("1005"+line.split(" ")[0].replace("-",""))
f.close()

#Open specific repLinks.txt file for each time folder 
for entry in dates:
    #Mention the correct path upto time folder name {0} and the following path to repLinks.txt in the line below
    f=open(PATH+"/{0}/communityStats".format(entry),"r") 
    t=open(PATH+"/{0}/communityStatsCorrected".format(entry),"a")
    t.write(f.readline())
    for line in f:
	line = line.strip()
	edges = line.split(' ')[2]
	density = line.split(' ')[3]
        com = line.split(' ')[0]   
	size = line.split(' ')[1]  
	if density == "NA": size = "3"
	print com,size,density
	t.write(com+" "+size+" "+edges+" "+density+"\n")
    f.close()
    t.close()
