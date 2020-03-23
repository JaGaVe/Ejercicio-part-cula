import numpy as np
from random import random


class Particula:

    __cuantas=0     #Atributo de clase

    def __init__(self):
        self.pos=np.array([0.0,0.0,0.0])
        self.vel=np.zeros(3)
        self.acc=np.zeros(3)
        Particula.__cuantas+=1

    def set_valores(self,pPos,pVel,pAcc):
        self.pos=pPos
        self.vel=pVel
        self.acc=pAcc

    def init_random(self):
        self.pos=np.array([random(),random(),random()])
        self.vel=np.array([random()*0.1,random()*0.1,random()*0.1])
        self.acc=np.array([random(),random(),random()])

    def distancia (self, otra):
        dif=self.pos-otra.pos
        return(dif[0]**2+dif[1]**2+dif[2]**2)**0.5

    def muestra (self):
        print('La posicion es: ', self.pos)
        print('La velocidad es: ', self.vel)
        print('La aceleracion es: ', self.acc, '\n')

    @classmethod
    def CuantasHay(cls):
        print('Se han definido: ', cls.__cuantas)


