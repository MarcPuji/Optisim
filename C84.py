import math

#[MIN] f (x,y)
#on f(x,y) = max { x2 + y2 ; x - 3y + 4 }

def f1(x,y):
	return x**2 + y**2
def f2(x,y):
	return x - 3*y + 4
def f(x,y):
	return max(f1(x,y),f2(x,y))
	
def preg4(v0,v1,v2):
	lg = []
	l1 = [f(v0[0],v0[1]),v0]
	l2 = [f(v1[0],v1[1]),v1]
	l3 = [f(v2[0],v2[1]),v2]
	lg.append(l1)
	lg.append(l2)
	lg.append(l3)
	lg.sort()
	vs = lg[0][1]
	vh = lg[1][1]
	vg = lg[2][1]
	
	v = ((v0[0] + v1[0] + v2[0])/2.0 , (v0[1] + v1[1] + v2[1])/2.0)
	vr = (2*v[0] - vg[0],2*v[1] - vg[1])
	
	return recu4(v,vr,vs,vh,vg,0)
	
def recu4(v,vr,vs,vh,vg,k):
	while k < 3:
		print([f(vs[0],vs[1]),f(vh[0],vh[1]),f(vg[0],vg[1])])
		fr = f(vr[0],vr[1]) 
		fs = f(vs[0],vs[1])
		fh = f(vh[0],vh[1])
		fg = f(vg[0],vg[1])
		if fr < fs:
			ve = (3*v[0] - 2*vg[0],3*v[1] - 2*vg[1])
			if f(ve[0],ve[1]) < f(vs[0],vs[1]):
				return recu4(v,vr,vs,vh,ve,k+1)
			else:
				return recu4(v,vr,vs,vh,vr,k+1)
		elif fs <= fr and fr < fh:
			return recu4(v,vr,vs,vh,vr,k+1)
		elif fh <= fr and fr < fg:
			return recu4(v,vg,vs,vh,vr,k+1)
		elif fr >= fg:
			return recu4(v,vg,vs,vh,vr,k+1)
	print([f(vs[0],vs[1]),f(vh[0],vh[1]),f(vg[0],vg[1])])




v0 = (0.8791, -0.4766)
v1 = (-0.0268, 0.9996)
v2 = (-0.8523, -0.5230)
print(preg4(v0,v1,v2))