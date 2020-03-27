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
        #Número de partículas
        for i in range(self.numParticulas):
            self.particulas.append(ParticulaMasa()) #Se crean los objetos y se introducen en la lista
        
        #Se inicializan con los datos dados (ver correo) para que no se salgan de los límites al graficar
        self.particulas[0].set_valores(np.zeros(3), np.zeros(3), np.zeros(3), 1.0e10)
        self.particulas[1].set_valores(np.array([1, 0., 0.]), np.array([0.,0.3,0.]), np.zeros(3), 5.0e8)
        self.particulas[2].set_valores(np.array([-0.9, 0., 0.]), np.array([0.,-0.3,0.]), np.zeros(3), 5.0e8)
        if self.numParticulas>3:
            for i in range(3,self.numParticulas):
                self.particulas.append(ParticulaMasa())
                self.particulas[i].init_random()

        """
        #Si inicializásemos las particulas aleatoriamente, con un número elegido al ejecutar. Se utilizarán solo 3 partículas para que no se salgan del grid
        for i in range(self.numParticulas):
            self.particulas.append(ParticulaMasa())
            self.particulas[i].init_random()
            self.particulas[i].acc=np.zeros(3)
        """

        """
        #Imprime las partículas, apra comprobar que se han añadido bien
        for i in range(self.numParticulas):
            print(self.particulas[i].pos)
            print(self.particulas[i].vel)
            print(self.particulas[i].acc)
            print(self.particulas[i].masa)
            print("\n")
        """
        self.prepara_grafico()
        self.refresca_particulas()
        
    def avanza (self):
        #Inicializar las aceleraciones a cero
        for i in range(self.numParticulas):
            self.particulas[i].acc=np.zeros(3)
    
        #Calcular aceleración producida por cada partícula y actualizar posición y velocidad. LA PARTICULA [0] NO SE ACTUALIZA
        for p1 in range(self.numParticulas):
            for p2 in range (self.numParticulas):
                self.particulas[p1].acc_gravitatoria(self.particulas[p2])
            self.particulas[p1].actualiza_velypos(self.deltat)
        self.particulas[0].set_valores(np.zeros(3), np.zeros(3), np.zeros(3), 1.0e10) #Vuelve a dejar a la partícula[0] como estaba
        self.refresca_particulas()  
      
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
        for _ in range(self.numParticulas-1):
            col.append('r')
        x,y,z=self.vectoriza() 
        self.grafico=self.ax.scatter(x,y,z,c=col,marker='o')
        plt.draw()
        plt.pause(0.05)

    def vectoriza(self):
        x,y,z=[],[],[]
        for i in range(self.numParticulas):
            x.append(self.particulas[i].pos[0])
            y.append(self.particulas[i].pos[1])
            z.append(self.particulas[i].pos[2])

        return x,y,z



    



    