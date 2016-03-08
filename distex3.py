import random

def exp(x=15):
	y = random.random()
	return float((-1/x)*math.log(y))
	
def uni():
	y = random.random()
	return float(10.0*y + 20.0)

def prova():
	y = random.random()
	if y < 0.8:
		return True
	else:
		return False
		
