import random

def trucada():
	a = 0
	b = 1/6.0
	y = random.random()
	for i in range(6):
		if y >= a and y < b:
			return (i+1)
		else:
			a = b
			b = (1/6.0)*(2+i)
	return 6
def consulta():
	y = random.random()
	if y < 0.6:
		return 2
	else:
		return 5