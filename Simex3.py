import distex3

def simex3(max_temps):
	global rellotge
	global n
	global PCT
	global PPT
	
	iniciar_variables()
	esdeveniment = obtenir_esdeveniment()
	
	while rellotge <= max_temps:
		
		rellotge = esdeveniment[0]
		tipus = esdeveniment[1]
		
		n += 1
		PCT += PC
		PPT += PP
		
		if tipus == 'arribada pacient':
			arribada_pacient()
		if tipus == 'sortida pacient':
			sortida_pacient()
		if tipus == 'sortida prova':
			sortida_prova()
		
	a = float(PCT/n)
	b = float(PPT/n)
	return [a,b]
	
def iniciar_variables():
	global rellotge
	global PC
	global PP
	global llista_esdeveniments
	global n
	
	rellotge = 0.0
	
	#consulta buida
	consulta = 1
	llista_esdeveniments = []
	PC = 0
	PP = 0
	afegir_arribada()
	
	#numero de vegades que mirem quants pacients esperen:
	n = 1
	#total de pacients esperant a consulta
	PCT = 0
	#total de pacients esperant a prova
	PPT = 0
	
def afegir_arribada():
	global llista_esdeveniments
	
	t = distex3.exp()
	llista_esdeveniments.append([rellotge + t, 'arribada consulta'])

def obtenir_esdeveniment():
	global llista_esdeveniments
	llista_esdeveniments.sort()
	esdeveniment = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment

def arribada_pacient():
	global rellotge
	global llista_esdeveniments
	global PC
	
	if PC < 3:
		t = distex3.uni()
		llista_esdeveniments.append([rellotge + t, 'sortida consulta'])
	PC += 1
	afegir_arribada()

def sortida_pacient():
	global llista_esdeveniments
	global rellotge
	global PC
	global PP
	
	if PC >= 3:
		t = distex3.uni()
		llista_esdeveniments.append([rellotge + t, 'sortida consulta'])
	if distex3.prova():
		if PP = 0:
			llista_esdeveniments.append([rellotge+10.0,'sortida prova'])
		PP += 1
	PC -= 1

def sortida_prova():
	global llista_esdeveniments
	global rellotge
	global PP
	
	if PP > 1:
		llista_esdeveniments.append([rellotge+10.0, 'sortida prova')]
	PP += 1
		
		
