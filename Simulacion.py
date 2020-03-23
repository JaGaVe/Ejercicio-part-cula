import numpy as np
from random import random
from Particula_masa import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class Simulacion():
    def __init__ (self, NumPart, t_total):
        self.numParticulas=NumPart
        self.tTotal=t_total
        self.deltat=0.1
        self.particulas=[]
        #Número de partículas, se inicializan con acc = 0
        for i in range(self.numParticulas):
            self.particulas.append(ParticulaMasa())
            self.particulas[i].init_random()
            self.particulas[i].acc=np.zeros(3)
            """
            print(self.particulas[i].pos)
            print(self.particulas[i].vel)
            print(self.particulas[i].acc)
            print(self.particulas[i].masa)
            print("\n")
            """
            self.prepara_grafico()
            self.refresca_particulas()
    def avanza (self):
        """
        #Inicializar las aceleraciones a cero
        for i in range(self.numParticulas):
            self.particulas[i].acc=np.zeros(3)
        """
        #Calcular aceleración producida por cada partícula y actualizar posición y velocidad.
        for p1 in range(self.numParticulas):
            for p2 in range (self.numParticulas):
                self.particulas[p1].acc_gravitatoria(self.particulas[p2])
            self.particulas[p1].actualiza_velypos(self.deltat)

    def simula (self):
        for i in np.arange(0.0,self.tTotal,self.deltat):
            self.avanza()
            s=('En la simulación con t='+str(i+self.deltat)+', la pos, vel y acc de las partículas es:' )
            print(s)
            for i in range(self.numParticulas):
                print('Partícula ', str(i+1), ':')
                print(self.particulas[i].pos)
                print(self.particulas[i].vel)
                print(self.particulas[i].acc)
                print(self.particulas[i].masa, "\n")
    #Prepar gráfico
    def prepara_grafico(self):
        plt.ion()
        self.fig=plt.figure()
        self.ax=self.fig.add_subplot(111,projection='3d')

        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)

        self.grafico=self.ax.scatter([],[],[],c='r',marker='o')

        plt.draw()
    
    def refresca_particulas(self):
        self.grafico.remove()   #Limpia el gráfico
        col=['g']
        for _ in range(self.numParticulas):
            col.append('r')
        x,y,z=self.vectoriza()  #Me falta este método ???
        self.grafico=self.ax.scatter(x,y,z,c=col,marker='o')
        plt.draw()
        plt.pause(0.1)


    



    