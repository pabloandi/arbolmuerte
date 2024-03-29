import pygame
from pygame.image import save
from arbol import Arbol


class Lienzo:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1920, 1080
        self.arbol = Arbol()

    def save_image(self):
        save(self._display_surf,'arbol.png')

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.save_image()

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(pygame.Color('white'))
        self.arbol.pintar(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:

            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    lienzo = Lienzo()
    lienzo.on_execute()
