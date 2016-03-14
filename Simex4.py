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
	
print(simex4(90))