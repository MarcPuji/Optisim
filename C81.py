import math

#f(x) = x3 + 1958 e-x
def f(x):
	return x**3 + 1958*math.exp(-x)

def preg1(x1,x2, n):
	r   = (math.sqrt(5) - 1)/2.0
	x3 = x2 - r*(x2-x1)
	x4 = x1 + r*(x2-x1)
	
	return recu1(r,f(x3),f(x4),x1,x2,x3,x4,1,n)

def recu1(r,fx3,fx4,x1,x2,x3,x4,k,n):
	if k <= n:
		if f(x3)<f(x4):
			x2 = x4
			x4 = x3
			x3 = x2 - r*(x2-x1)
			print(x1,x2)
			k = k + 1
			recu1(r,f(x3),fx4,x1,x2,x3,x4,k,n)
		
		else:
			x1 = x3
			x3 = x4
			x4 = x1 + r*(x2-x1)
			print(x1,x2)
			k = k + 1
			recu1(r,fx3,f(x4),x1,x2,x3,x4,k,n)
			

x1 = 3.0219
x2 = 4.9893
preg1(x1,x2,3)