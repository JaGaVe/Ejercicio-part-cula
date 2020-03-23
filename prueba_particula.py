from particula import *
from Particula_masa import *

""" 
Ejercicio 2.1

p1=Particula()
p2=Particula()
p3=Particula()

p2.set_valores(np.array([3.0,4.0,0.0]),np.zeros(3),np.zeros(3))
p3.init_random()

p1.muestra()
p2.muestra()
p3.muestra()

print('distancia: ',p1.distancia(p2))
"""

#Ejercicio 2.2
dt=0.1

p1=ParticulaMasa()
p2=ParticulaMasa()

p2.init_random()
p2.muestra()

p1.set_valores(np.array([3.0,4.0,0.0]),np.zeros(3),np.zeros(3),2.8e-6)
p1.muestra()

p1.acc_gravitatoria(p2)
p2.acc_gravitatoria(p1)

p1.actualiza_velypos(dt)
p2.actualiza_velypos(dt)

p1.muestra()
p2.muestra()

Particula.CuantasHay()
