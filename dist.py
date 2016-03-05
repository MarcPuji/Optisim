import random

def uniforme_discreta(a=3,b=7):
	return int(a + (b+1-a)*random.random())

def discreta_arbitraria2(p1=0.33):
	y = random.random()

	if y < p1 :
		return 2

	if y >= p1:
		return 3
