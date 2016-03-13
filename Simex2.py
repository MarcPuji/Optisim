import distex2

def simex2(max_temps):
	global rellotge
	global nc
	global PE
	
	iniciar_variables()
	esdeveniment = obtenir_esdeveniment()
	
	temps_espera_total=0.0
	esdeveniment_anterior=0.0
	
	while rellotge <= max_temps:
		
		rellotge = esdeveniment[0]
		tipus = esdeveniment[1]
		
		temps_espera = rellotge-esdeveniment_anterior
		if PE > 1:
			temps_espera_total += temps_espera*(PE-1)
		
		
		if tipus == 'arribada trucada':
			arribada_trucada()
		if tipus == 'acaba consulta':
			sortida_trucada()
		
		esdeveniment = obtenir_esdeveniment()
		esdeveniment_anterior=rellotge
		
	return float(temps_espera_total/nc)

def iniciar_variables():
	global PE
	global rellotge
	global llista_esdeveniments
	global nc
	
	rellotge = 0.0
	PE = 0
	nc = 0
	
	llista_esdeveniments = []
	afegir_trucada()
	
def obtenir_esdeveniment():
	global llista_esdeveniments
	llista_esdeveniments.sort()
	esdeveniment = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment
	
def afegir_trucada():
	global llista_esdeveniments
	global rellotge
	
	t = distex2.trucada()
	llista_esdeveniments.append([rellotge + t, 'arribada trucada'])

def arribada_trucada():
	global llista_esdeveniments
	global rellotge
	global PE
	global nc
	
	if PE == 0:
		t = distex2.consulta()
		llista_esdeveniments.append([rellotge + t, 'acaba consulta'])
	PE += 1
	afegir_trucada()
	nc += 1
	
def sortida_trucada():
	global llista_esdeveniments
	global rellotge
	global PE
	
	if PE > 1:
		t = distex2.consulta()
		llista_esdeveniments.append([rellotge+t,'acaba consulta'])
	PE -= 1
	
	
def escriu():
	f = open('ex2.txt','w')
	for i in range(1000):
		 e = str(simex2(12*60))
		 e = e.split('.')
		 e = ','.join(e)
		 f.write(e + '\n')
	f.close()
	
escriu()
