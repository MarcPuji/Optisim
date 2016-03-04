from dist import uniforme_discreta
from dist import discreta_arbitraria2


def Simular_Munta(maxim_temps):
	global rellotge
	global estat
	global caixes
	
	iniciar_variables()
	esdeveniment = obtenir_esdeveniment()
	
	while rellotge < maxim_temps:
		rellotge = esdeveniment[0]
		tipus_esdeveniment = esdeveniment[1]
		if tipus_esdeveniment == 'arribada A':
			arribada_A()
		
	
def iniciar_variables():
	global estat
	global llista_esdeveniments
	global caixes
	global rellotge
	
	rellotge=0.0
	
	estat = 1
	#el muntacarregues esta disponible
	llista_esdeveniments = []
	caixes = {'A':[0,0,0] , 'B':[0,0,0] , 'C':[0,0,0]}
	#diccionari on les claus son el tipus de caixa i els valors corresponen a
	#nombre de caixes en espera
	#temps total d'espera
	#nombre total de caixes
	afegir_arribada_caixaA()
	afegir_arribada_caixaB()
	afegir_arribada_caixaC()
	#primers esdeveniments d'arribades de caixes

def afegir_arribada_caixaA():
	global llista_esdeveniments
	global rellotge
	
	t_a = uniforme_discreta(3,7)
	t    = rellotge + t_a
	llista_esdeveniments.append([t,'arribada A'])
	
def afegir_arribada_caixaB():
	global llista_esdeveniments
	global rellotge
	
	t = rellotge + 6
	llista_esdeveniments.append([t,'arribada B'])
	
def afegir_arribada_caixaC():
	global llista_esdeveniments
	global rellotge
	
	t_c= discreta_arbitraria2(0.33,0.67)
	t = rellotge + t_c
	llista_esdeveniments.append([t,'arribada C'])
	
	
def obtenir_esdeveniment():
	global llista_esdeveniments
	llista_esdeveniments.sort()
	esdeveniment = llista_esdeveniments[0]
	llista_esdeveniments = llista_esdeveniments[1:]
	return esdeveniment

def arribada_A():
	global caixes
	global estat
	
	caixes['A'][0] += 1
	caixes['A'][2] += 1
	#actualitza el nombre de caixes
	
	if estat == 0 and possible_carregar():
		
		carrega()
		
	afegir_arribada_caixaA()

def possible_carregar():
	global caixes 
	
	pes = caixes['A'][0]*200+caixes['B'][0]*100+caixes['C'][0]*50
	
	return pes >= 400
	
