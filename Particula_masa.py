from scipy import constants
import numpy as np
from random import random
from particula import *

class ParticulaMasa(Particula):
    def __init__(self):
        self.masa=0.0
        super().__init__()
    
    def set_valores(self,pPos,pVel,pAcc,pMasa):
        self.masa=pMasa
        super().set_valores(pPos,pVel,pAcc)

    def init_random(self):
        self.masa=random()*1e6

    def muestra(self):
        print('La masa es: ', self.masa)
        super().muestra()

    def acc_gravitatoria (self, otra):
        G=constants.gravitational_constant
        delta=otra.pos-self.pos
        dist=self.distancia(otra)
        softening=1e-2          #Evita que el programa de error al hacer la inversa de distancia
        if dist<softening:
            dist=softening
        distInv=(1/dist)**3
        self.acc+=G*self.masa*distInv*delta

    def actualiza_velypos(self,deltat):
        self.vel+=self.acc*deltat
        self.pos+=self.vel*deltat
    




        

    
