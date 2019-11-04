import sys
import numpy as np
import readfile as rd


def freq_cal(data,mn,mx):
	c=0
	for i in range(len(data)):
		if(data[i]>=mn and data[i]<mx):
			c=c+1
	return c
	
def parameter_uniform(data):
	mean1=np.mean(data)
	var=np.var(data)
	b=(2*mean1+np.sqrt(var*12))/2
	a=2*mean1-b
	return a,b
		
		

def uniform_distrubution(data,interval):
	n=len(data)
	print(n)
	p=1/interval
	ai=[]
	oj=[]
	ojej=[]
	ej=n/interval
	mn=min(data)
	mx=max(data)+1
	a,b=parameter_uniform(data)
	for i in range(1,interval):
		aii=a+(b-a)*i*p
		ai.append(aii)
		ojj=freq_cal(data,mn,aii)
		oj.append(ojj)
		ojej.append((ojj-ej)**2/ej)
		mn=aii
	aii=a+(b-a)*i*p
	ai.append(aii)
	ojj=freq_cal(data,aii,mx)
	oj.append(ojj)
	ojej.append((ojj-ej)**2/ej)
	for i in range(len(oj)):
		print(i,ai[i],oj[i],ojej[i])	
	#print(ai,oj,ojej)
	print(sum(oj))
	print(sum(ojej))

filename=sys.argv[1]
interval=int(sys.argv[2])
data=rd.readFile_txt(filename)
uniform_distrubution(data,interval)



