import Munta

def escriu(n):
	
	fa = open('CaixesA.txt','w')
	fb = open('CaixesB.txt','w')
	fc = open('CaixesC.txt','w')
	
	for i in range(n):
		lla = []
		llb = []
		llc = []
		
		c = Munta.Simular_Munta()
		
		lla.append(c[0])
		llb.append(c[1])
		llc.append(c[2])
		
		ma = str(sum(lla)/len(lla))
		mb = str(sum(llb)/len(llb))
		mc = str(sum(llc)/len(llc))
		
		ma = ma.split('.')
		ma = ','.join(ma)
		mb = mb.split('.')
		mb = ','.join(mb)
		mc = mc.split('.')
		mc = ','.join(mc)
		
		fa.write(str(ma) + '\n')
		fb.write(str(mb) + '\n')
		fc.write(str(mc) + '\n')
	fa.close()
	fb.close()
	fc.close()


escriu(100)