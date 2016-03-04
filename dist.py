import random


def uniforme_discreta(a,b):
	return int(a + (b+1-a)*random.random())

def discreta_arbitraria2(p1):
	y = random.random()
	if y < p1 :
		return 2
	if y >= p1:
		return 3