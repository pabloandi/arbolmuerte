from pygame.font import SysFont
from pygame.color import Color


class Aminoacido:
    """Clase Aminoácido para dibujar el color y establecer la letra"""

    font = SysFont("monospace", 12)

    def __init__(self, screen, aminoacido, pos):
        self.screen = screen
        self.posicion = pos
        self.aminoacido = aminoacido
        self.paso = 5

        self.A = Color('GREEN')
        self.T = Color('RED')
        self.G = Color('YELLOW')
        self.C = Color('BLUE')
        self.U = Color('ORANGE')
        self.otro = Color('GREY')
        self.color = None
        self.setColorPosicion(aminoacido)
        self.draw()

    def setColorPosicion(self, aminoacido):
        x,y= self.posicion
        paso = self.paso

        if aminoacido == 'A':
            self.color = self.A
            self.posicion = x-paso,y
        elif aminoacido == 'T':
            self.color = self.T
            self.posicion = x - paso, y - paso
        elif aminoacido == 'G':
            self.color = self.G
            self.posicion = x + paso, y - paso
        elif aminoacido == 'C':
            self.color = self.C
            self.posicion = x + paso, y
        elif aminoacido == 'U':
            self.color = self.U
            self.posicion = x, y + paso
        else:
            self.color = self.otro
            self.posicion = x, y + paso


    def draw(self):
        Aminoacido.font.render_to(surf=self.screen, dest=self.posicion, text=self.aminoacido, fgcolor=self.color)
