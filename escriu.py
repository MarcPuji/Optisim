import Munta_final

def escriu(n):
	
	fa = open('CaixesA.txt','w')
	fb = open('CaixesB.txt','w')
	fc = open('CaixesC.txt','w')
	
	for i in range(n):
		
		c = Munta_final.Simular_Munta(8*60)
		ma = str(c[0])
		mb = str(c[1])
		mc = str(c[2])
		
		ma = ma.split('.')
		ma = ','.join(ma)
		mb = mb.split('.')
		mb = ','.join(mb)
		mc = mc.split('.')
		mc = ','.join(mc)
		
		fa.write(ma + '\n')
		fb.write(mb + '\n')
		fc.write(mc + '\n')
		
	fa.close()
	fb.close()
	fc.close()

escriu(10000)
