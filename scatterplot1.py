import matplotlib
from matplotlib import pyplot as pl
import readfile as rd
import sys

def scatterplot(data):
	for i in range(len(data)-1):
		pl.plot(data[i],data[i+1],'bo')
	pl.show()
	
def freq(diff_table,mn,mx):
	c=0
	for i in range(len(diff_table)):
		if(diff_table[i]>=mn and diff_table[i]<mx):
			c=c+1
	return c

def bargraph(data,interval):
	min1=min(data)
	max1=max(data)
	d=(max1-min1)/interval
	oj=[]
	ai=[]
	while(min1<max1):	
		ai.append(min1)
		oj.append(freq(data,min1,min1+d))
		min1=min1+d
	print(ai,oj)
	pl.bar(ai,oj,1)
	pl.show()
		
		
	
fm=sys.argv[1]
interval=int(sys.argv[2])
data=rd.readFile_txt(fm)
#scatterplot(data)
bargraph(data,interval)		
