from Simulacion import *

NumParticulas=int(input("Introduce número de partículas: "))
TiempoTot=int(input("Introduce tiempo total: "))

sim=Simulacion(NumParticulas,TiempoTot)
sim.simula()