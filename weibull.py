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
def fun_g_of_alpha(data,alpha,n):
	var=0.0
	var1=0.0
	var2=0.0
	var3=0.0
	for i in range(n):
		var1=var+data[i]**alpha*np.log(data[i])
		var2=var2+data[i]**alpha
	var3=(n*var1)/var2
	
	var=n/alpha+np.mean(np.log(data))-(var3)
	return var

def fun_g_dash_of_alpha(data,alpha,n):
	for i in range(n):
		var1=0.0
		var2=0.0
		var=0.0
		var1=var1+data[i]*(np.log(data[i]))**2
		var2=var2+((data[i])**alpha)*(np.log(data[i]))**2
		var=var+(data[i])**alpha
	ret_value=(-n/(alpha)**2)-((n*var1)/(var)+(n*var2)/(var)**2)
	return ret_value

def parameter_weibull(data):
	mean=np.mean(data)
	var=np.var(data)
	alpha0=mean/var
	alpha=0.0
	var=0.0
	n=len(data)
	while(alpha<0.001):
		alpha=alpha0-(fun_g_of_alpha(data,alpha0,n)/fun_g_dash_alpha(data,alpha0,n))
		alpha0=alpha
	for i in range(n):
		var=var+data[i]**alpha
	
	beta=(1/n)*(var)**(1/alpha)
	return alpha,beta

def weibull_fun(alpha,beta,x):
	ret_value=(alpha*beta**(-alpha))*x**(alpha-1)*np.exp(-(x/beta)**alpha)
	
def weibull(data,interval):
	alpha,beta=parameter_weibull(data)
	min1=min(data)
	max1=max(data)
	d=(max1-min1)/interval
	h=d/100
	p=0.0
	ai=[]
	oj=[]
	ojej=[]
	while(min1<max1):
		summetion=0.0
		i=1
		ai.append(min1+d)
		oj.append(freq_cal(data,min1,min1+d))
		mn=min1
		while(i<100):
			summetion=summetion+weibull_fun(aplha,beta,mn+h)
			mn=mn+h
			i=i+1
		p=(h/2)*((weibull_fun(alpha,beta,min1)+weibull_fun(alpha,beta,min1+d))+2*summetion)
		ej.append(n*p)	
		min1=min1+d
	for i in range(len(oj)):
		ojej.append(((oj[i]-ej[i])**2)/ej[i])
	print(sum(ojej))


fm=sys.argv[1]
interval=int(sys.argv[2])
data=rd.readFile_csv(fm)
weibull(data,interval)
	
