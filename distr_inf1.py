import random
import math

def triangular(a,b,c):
	y = random.random()
	if y >= 0 and y < (c-a)/(b-a):
		return float(a+math.sqrt((b-a)*(c-a)*y))
	if y >= (c-a)/(b-a):
		return float(b-math.sqrt((b-a)*(b-c)*(1-y)))
		

def normal(x,o):
	y1 = random.random()
	y2 = random.random()
	t = math.sqrt(-2*math.log(y1))*math.sin(2*math.pi*y2)
	t2 = math.sqrt(-2*math.log(y1))*math.cos(2*math.pi*y2)
	return float(x+t*o)

def discreta_arbitraria2(p1,p2):
	y = random.random()
	if y >= p1 and y < p2:
		return 1
	if y > p2:
		return 2

def continua_exp(x):
	y = random.random()
	return float((-1/x)*math.log(x))
	
def normal_convertida(nom,x,o):
	doc = open(nom,'w')
	i = 0
	while i <100:
		n = normal(x,o)
		ns = str(n)
		doc.write(ns + '\n')
		i += 1
	doc.close()

def triangular_convertida(nom,a,b,c):
	doc = open(nom,'w')
	i = 0
	while i <100:
		n = triangular(a,b,c)
		ns = str(n)
		ns.split('.')
		','.join(ns)
		doc.write(ns + '\n')
		i += 1
	doc.close()

def disar_convertida(nom,p1,p2):
	doc = open(nom,'w')
	i = 0
	while i <100:
		n = discreta_arbitraria2(p1,p2)
		ns = str(n)
		ns.split('.')
		','.join(ns)
		doc.write(ns + '\n')
		i += 1
	doc.close()

def exp_convertida(nom,x):
	doc = open(nom,'w')
	i = 0
	while i <100:
		n = continua_exp(x)
		ns = str(n)
		ns.split('.')
		','.join(ns)
		doc.write(ns + '\n')
		i += 1
	doc.close()