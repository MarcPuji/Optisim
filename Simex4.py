import distex4

def simex4(dies):
	
	demanda = distex4.demanda()
	total_falten = 0
	if demanda > 15:
		falten = demanda - 15
		total_falten = falten
	demanda_total = demanda
	d = 2	
	
	while d <= dies:
		demanda = distex4.demanda()
		if demanda > 20:
			falten = demanda - 20
			total_falten += falten
		demanda_total += demanda
		d += 1
	return float(total_falten/demanda_total)

def mitjanes():
	l = []
	for i in range(100):
		m = simex4(60)
		l.append(m)
	return (sum(l)/100)	
def escriu():
	f = open('ex4.txt.','w')
	for i in range(100):
		t = str(mitjanes())
		t = t.split('.')
		t = ','.join(t)
		f.write(t + '\n')
	f.close()
escriu()