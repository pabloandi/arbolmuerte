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

    def leer_archivo(self):
        try:
            self.secuencia = SeqIo.read(archivo,'genbank').seq
        except Exception as e:
            pass

    def crear_camino(self):
        r=0
        theta=0

        for aminoacido in self.secuencia:
            x = r * cos(theta)
            y = r * sin(theta)

            Aminoacido(self.screen, aminoacido, (x,y))

            r += 0.02
            theta += 0.02

    def draw(self):
        pass

if __name__ == '__main__':
    pass