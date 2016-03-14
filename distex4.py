import math
import random

def demanda():
	y1 = random.random()
	y2 = random.random()
	tt = math.sqrt(-2*math.log(y1))*math.sin(2*math.pi*y2)
	t = (tt*3+15)
	if t >= 0 and t <= 25:
		return int(t)
	elif t < 0:
		return 0
	else:
		return 25