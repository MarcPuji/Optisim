import math

#f(x) = x3 + 1696 e-x
def f(x):
	return x**3 + 1696*math.exp(-x)
def fp(x):
	return 3*x**2 - 1696*math.exp(-x)
def fp2(x):
	return 6*x + 1696*math.exp(-x)

def preg3(x1,k,n):
	if k <= n:
		x1 = x1 - (fp(x1)/fp2(x1))
		print(x1)
		return preg3(x1,k+1,n)

x1 = 17.4704
k  = 1
n = 3

preg3(x1,k,n)