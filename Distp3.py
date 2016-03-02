import random


def uniforme_discreta(a,b):
    return int(a + (b+1-a)*random.random())

def discreta_arbitraria2(p1,p2):
	y = random.random()
	if y >= p1 and y < p2:
		return 1
	if y > p2:
		return 2