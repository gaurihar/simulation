import sys
import numpy as np
import math
import readfile as rd


def freq_cal(data,mn,mx):
	c=0
	for i in range(len(data)):
		if(data[i]>=mn and data[i]<mx):
			c=c+1
	return c

def expontial_fun(lamda,x):
	ret_value=lamda*np.exp(-lamda*x)
	return ret_value
	

def parameter_exp(data):
	beta=np.mean(data)	
	return beta


def chiSq_expontial(data,interval):
	min1=min(data)
	max1=max(data)
	print(min1,max1)
	d=(max1-min1)/interval
	n=len(data)
	ai=[]
	oj=[]
	ej=[]
	ojej=[]
	ojej1=0.0
	h=d/100
	beta = parameter_exp(data)
	lamda = 1/beta
	while(min1<max1):
		ai.append(min1)
		oj1=freq_cal(data,min1,min1+d)
		oj.append(oj1)
		mn=min1
		#print(min1,mn)
		summetion=0.0
		i=1
		while(i<100):
			#print(mn)
			summetion=summetion+expontial_fun(lamda,mn+h)
			#print(summetion)
			mn=mn+h
			i=i+1
			
		p=(h/2)*((expontial_fun(lamda,min1)+expontial_fun(lamda,min1+d))+2*summetion)
		ej1=n*p
		ej.append(ej1)
		ojej1=(oj1-ej1)**2/ej1
		ojej.append(ojej1)
		min1=min1+d
	for i in range(len(oj)):
		print(i,ai[i] ,oj[i] ,ej[i] ,ojej[i])
	print(sum(ojej),sum(oj))



filename=sys.argv[1]
interval=int (sys.argv[2])
data=rd.readFile_txt(filename)
chiSq_expontial(data,interval)
		
