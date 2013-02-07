import sys

PATH = sys.argv[1]
dirname = sys.argv[2]
PATH = PATH+'/'+dirname
M = sys.argv[3] # number of communities

t = open("PATHSplusCOMS","a")
#t = open("PATHS","a")

t.write(PATH+'\t'+M+'\n')
#t.write(PATH+'\n')
t.close()
