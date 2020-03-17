from pathlib import Path
from rama import Rama

import pygame

class Arbol:
    """Lee los archivos de las secuencias de adn y crea ramas con cada uno"""
    def __init__(self):
        self.pathvirus = Path("./material/virus").resolve()
        self.pathbacterias = Path("./material/bacteria").resolve()
        self.archivos_secuencias = [archivo for archivo in self.pathvirus.iterdir()] + [archivo for archivo in self.pathbacterias.iterdir()]


    def pintar(self, screen):
        self.screen = screen
        self.pintar_tronco()
        self.pintar_ramas()

    def pintar_tronco(self):
        MARRON =  pygame.Color('BROWN')
        ancho, alto = self.screen.get_size()
        pygame.draw.rect(self.screen, MARRON, (
            # TODO implementar con las medidas del screen

            (ancho // 2) - 50, alto, 100, -100
        ))

    def pintar_ramas(self):
        # pass
        for secuencia in self.archivos_secuencias[:10]:
            Rama(self.screen, secuencia)

if __name__ == '__main__':
    arbol = Arbol()
    print(arbol.archivos_secuencias)