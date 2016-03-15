import math

#f(x) = x3 + 1958 e-x
def f(x):
	return x**3 + 1958*math.exp(-x)
def fp(x):
	return 3*(x**2) - 1958*math.exp(-x)

def preg2(x1,x2,n):
	k = 1
	return recu2(x1,x2,k,n)
		
def recu2(x1,x2,k,n):
	fpm = fp(((x1+x2)/2.0))
	if k <= n:
		if fpm > 0:
			x2 = (x1+x2)/2.0
			print(x1,x2)
			return recu2(x1,x2,k+1,n)
		if fpm < 0:
			x1 = (x1+x2)/2.0
			print(x1,x2)
			return recu2(x1,x2,k+1,n)
		if fpm == 0:
			return (x1+x2)/2.0

x1 = 
x2 = 
n = 3
preg2(x1,x2,n)