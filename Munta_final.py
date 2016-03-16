from dist import uniforme_discreta
from dist import discreta_arbitraria2


def Simular_Munta(maxim_temps):
	global rellotge
	global estat
	global caixes
	global llista_esdeveniments
	
	#inciem les variables amb els valors desitjats
	iniciar_variables()
	esdeveniment = obtenir_esdeveniment()
	esdeveniment_anterior=0.0
	
	#el bucle s'atura quan es rebassa el temps de simulacio estipulat
	while rellotge <= maxim_temps:

		#cada esdeveniment es una llista amb el temps associat en primera posicio i el tipus d'esdeveniment en segona
		rellotge = esdeveniment[0]
		tipus_esdeveniment = esdeveniment[1]

		#actualitzem el temps d'espera per cada caixa ( temps anterior d'espera + temps de succes entre esdeveniments*nombre de caixes en espera de cada tipus)
		temps_espera = rellotge-esdeveniment_anterior

		caixes['A'][1], caixes['B'][1], caixes['C'][1] = caixes['A'][1]+caixes['A'][0]*temps_espera, caixes['B'][1]+caixes['B'][0]*temps_espera, caixes['C'][1]+caixes['C'][0]*temps_espera
		
		
		

		#assignem per cada tipus d'esdeveniments les consequencies generades, hem definit una funcio per cada esdeveniment
		if tipus_esdeveniment == 'arribada A':
			arribada_A()
		if tipus_esdeveniment == 'arribada B':
			arribada_B()
		if tipus_esdeveniment == 'arribada C':
			arribada_C()
		if tipus_esdeveniment == 'Muntacarregues disponible':
			arribada_muntacarregues()


		#obtenim el seguent esdeveniment 
		esdeveniment = obtenir_esdeveniment()

		#gravem el temps de l'esdeveniment anterior abans de comencar el seguent pas iteratiu
		esdeveniment_anterior=rellotge
		
	#un cop s'ha acabat la jornada laboral, encara queden caixes pendents
	caixes_pendents = caixes['A'][0] + caixes['B'][0] + caixes['C'][0]
	
	while caixes_pendents > 0:
		rellotge = esdeveniment[0]
		tipus_esdeveniment = esdeveniment[1]
		
		temps_espera = rellotge-esdeveniment_anterior
		caixes['A'][1], caixes['B'][1], caixes['C'][1] = caixes['A'][1]+caixes['A'][0]*temps_espera, caixes['B'][1]+caixes['B'][0]*temps_espera, caixes['C'][1]+caixes['C'][0]*temps_espera
		
		if tipus_esdeveniment == 'Muntacarregues disponible':
			arribada_muntacarregues()
		
		caixes_pendents = caixes['A'][0] + caixes['B'][0] + caixes['C'][0]
		
		if final():
			if estat == 0:
				for i in range(len(llista_esdeveniments)):
					if llista_esdeveniments[i][1] == 'Muntacarregues disponible':
						t = llista_esdeveniments[i][0]
				temps_espera = t-rellotge
				caixes['A'][1], caixes['B'][1], caixes['C'][1] = caixes['A'][1]+caixes['A'][0]*temps_espera, caixes['B'][1]+caixes['B'][0]*temps_espera, caixes['C'][1]+caixes['C'][0]*temps_espera
			caixes_pendents = 0
		
		if len(llista_esdeveniments) > 0:
			esdeveniment = obtenir_esdeveniment()
		esdeveniment_anterior = rellotge
		
	#retorna el valor d'espera promig per cada caixa (temps d'espera global de cada tipus/nombre de caixes de cada tipus)
	return caixes['A'][1]/caixes['A'][2], caixes['B'][1]/caixes['B'][2], caixes['C'][1]/caixes['C'][2]

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
	
	t_a = uniforme_discreta()
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
	
	t_c= discreta_arbitraria2()
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
	
	if possible_carregar():
		
		carrega()
		
	afegir_arribada_caixaA()


def arribada_B():
	global caixes
	global estat
	
	caixes['B'][0] += 1
	caixes['B'][2] += 1
	#actualitza el nombre de caixes
	
	if possible_carregar():
		
		carrega()
		
	afegir_arribada_caixaB()


def arribada_C():
	global caixes
	global estat
	
	caixes['C'][0] += 1
	caixes['C'][2] += 1
	#actualitza el nombre de caixes
	
	if possible_carregar():
		
		carrega()
		
	afegir_arribada_caixaC()

def possible_carregar():
	global caixes 
	
	pes = caixes['A'][0]*200+caixes['B'][0]*100+caixes['C'][0]*50
	
	#mirem que el pes disponible sigui major que 400 i que estigui disponible el muntacarregues
	return pes >= 400 and estat == 1

def carrega():
	global caixes
	global llista_esdeveniments
	global rellotge
	global estat

	estat = 0
	#proces d'ordenacio de caixes per ordre sequencial i ordenats de major nombre a menor, donant prioritat a les caixes mes grans en cas d'empat
	#8 caixes (8*50)
	if caixes['C'][0] >= 8:
		caixes['C'][0]-=8 

	#7 caixes (6*50+1*100)
	elif caixes['C'][0] >= 6 and caixes['B'][0]>=1:
		caixes['C'][0]-=6
		caixes['B'][0]-=1

	#6 caixes (4*50+2*100)
	elif caixes['C'][0] >= 4 and caixes['B'][0]>=2:
		caixes['C'][0]-=4
		caixes['B'][0]-=2

	#5 caixes (4*50+1*200 / 2*50+3*100)
	elif caixes['C'][0]>=4 and caixes['A'][0]>=1:
		caixes['C'][0]-=4
		caixes['A'][0]-=1
	
	elif caixes['C'][0]>=2 and caixes['B'][0]>=3:
		caixes['C'][0]-=2
		caixes['B'][0]-=3

	#4 caixes (2*50+1*100+1*200 / 4*100)
	elif caixes['C'][0]>=2 and caixes['B'][0]>=1 and caixes['A'][0]>=1:
		caixes['C'][0]-=2
		caixes['B'][0]-=1
		caixes['A'][0]-=1
	elif caixes['B'][0]>=4:
		caixes['B'][0]-=4

	#3 caixes (2*100+2*200)
	elif caixes['B'][0]>=2 and caixes['A'][0]>=1:
		caixes['B'][0]-=2
		caixes['A'][0]-=1
	
	#2 caixes (2*200)
	elif caixes['A'][0]>=2:
		caixes['A'][0]-=2
	
	llista_esdeveniments.append([rellotge+4.0,'Muntacarregues disponible'])

def arribada_muntacarregues():
	global estat
	
	#actualitzem la variable per tal que l'ascensor estigui disponible
	estat = 1
	
	#mirem si es possible carregar el muntacarregues i si ho es ho fem
	if possible_carregar():
		carrega()


def final():
	global caixes
	
	pes = caixes['A'][0]*200+caixes['B'][0]*100+caixes['C'][0]*50
	
	return (pes<400)