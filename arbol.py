from pathlib import Path
from rama import Rama

import pygame

class Arbol:
    """Lee los archivos de las secuencias de adn y crea ramas con cada uno"""

    def __init__(self):
        """Inicializa el arbol leyendo las carpetas de las secuencias de virus y bacterias"""
        self.pathvirus = Path("./material/virus").resolve()
        self.pathbacterias = Path("./material/bacteria").resolve()
        self.archivos_secuencias = [archivo for archivo in self.pathvirus.iterdir()] + [archivo for archivo in self.pathbacterias.iterdir()]
        # limitar el número de secuencias con el proposito de optimizacion de recursos de máquina
        self.limite_secuencias = 50


    def pintar(self, screen):
        """Pintar todos los elementos del arbol"""
        self.screen = screen
        self.pintar_tronco()
        self.pintar_ramas()

    def pintar_tronco(self):
        """Pintar el tronco del arbol"""
        MARRON =  pygame.Color('BROWN')
        ancho, alto = self.screen.get_size()
        #
        pygame.draw.rect(self.screen, MARRON, (
            (ancho // 2) - 25, alto, 50, -50
        ))

    def pintar_ramas(self):
        """Pinta las ramas del arbol. Cada rama es una secuencia ADN de virus o bacteria"""
        for secuencia in self.archivos_secuencias[:self.limite_secuencias]:
            Rama(self.screen, secuencia)
