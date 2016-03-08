import random

def trucada():
	a = 0
	b = 1/6.0
	y = random.random()
	for i in range(6):
		if y >= a and y < b*(i+1):
			return (i+1)
		else:
			a = b
			b = (1/6.0)*(1+i)
			
def consulta():
	y = random.random()
	if y < 0.6:
		return 2
	else:
		return 5