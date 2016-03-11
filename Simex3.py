import distex3

def simex3(max_temps):
	global rellotge
	global PP
	global PC
	
	iniciar_variables()
	esdeveniment = obtenir_esdeveniment()
	t_anterior = 0.0
	
	while rellotge <= max_temps:
		
		pacients_esperant = 0
		rellotge = esdeveniment[0]
		tipus = esdeveniment[1]
		
		t_espera = rellotge - t_anterior
		if PC > 2:
			pacients_esperant = PC - 2
		if PP > 1:
			pacients_esperant = pacients_esperant + PP - 1
		
		if tipus == 'arribada pacient':
			arribada_pacient()
		if tipus == 'sortida consulta':
			sortida_consulta()
		if tipus == 'sortida prova':
			sortida_prova()
		
		esdeveniment = obtenir_esdeveniment()
		t_anterior = rellotge

	while PC > 0 and PP > 0:
		
		rellotge = esdeveniment[0]
		tipus = esdeveniment[1]
		
		if tipus == 'sortida consulta':
			sortida_consulta()
		if tipus == 'sortida prova':
			sortida_prova()
			
	return (t_espera_total/rellotge)
	
def iniciar_variables():
	global rellotge
	global PC
	global PP
	global llista_esdeveniments
	
	rellotge = 0.0
	
	#consulta buida
	consulta = 1
	llista_esdeveniments = []
	PC = 0
	PP = 0
	afegir_arribada()

	
def afegir_arribada():
	global llista_esdeveniments
	
	t = distex3.exp()
	llista_esdeveniments.append([rellotge + t, 'arribada pacient'])

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

def sortida_consulta():
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
		
		
