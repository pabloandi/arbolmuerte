from Bio.Seq import Seq
from Bio import SeqIO

from math import sin, cos
from aminoacido import Aminoacido
from math import sin,cos

import pygame

class Rama:

    def __init__(self, screen, archivo ):
        self.archivo = archivo
        self.secuencia = []
        self.camino = []
        self.screen = screen
        self.limites = screen.get_size()
        self.leer_archivo()
        self.crear_camino()

    def leer_archivo(self):
        try:
            self.secuencia = SeqIO.read(self.archivo,'genbank').seq
        except Exception as e:
            pass

    def crear_camino(self):
        limx,limy = self.limites
        partx = int(limx/2)
        x,y=partx,limy-200

        for aminoacido in self.secuencia[:100]:

            am=Aminoacido(self.screen, aminoacido, (x,y))
            x,y = am.getPosicionActual()



    def draw(self):
        pass

if __name__ == '__main__':
    pass