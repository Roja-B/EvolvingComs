#!/usr/bin/python
# this code removes punctuation and changes all tabs and whitespaces to one whitespace
import re,os,sys

def noPunct(filename):
	f = open(filename,"r")
	t = open(filename+"noPunct","w")
	for line in f:
		line = re.sub('[\.,-\/#?!$%\^&\*;:{}=\-_`~()"]',"",line)
		line = re.sub('[ \t]+'," ",line)
		t.write(line)
	return filename+"noPunct"
	f.close()
	t.close()
