from Bio import SeqIO

from aminoacido import Aminoacido

class Rama:
    """
    Cada rama del arbol esta asociada a una secuencia de ADN.
    El archivo de la secuencia de ADN está en formato Genbank.
    La mayoría de los archivos provienen de NCBI Genome Project
    https://www.ncbi.nlm.nih.gov/genome/

    """
    def __init__(self, screen, archivo ):
        self.archivo = archivo
        self.secuencia = []
        self.camino = []
        self.screen = screen
        self.limites = screen.get_size()
        self.limite_aminoacidos = 150
        self.leer_archivo()
        self.crear_camino()
        

    def leer_archivo(self):
        """
        Lee el archivo de la secuencia con la que fue
        asociado esta rama
        :return:
        """
        try:
            self.secuencia = SeqIO.read(self.archivo,'genbank').seq
        except Exception as e:
            pass

    def crear_camino(self):
        """
        Crea el camino de la secuencia.
        Inicia a partir del tope del tronco del arbol
        :return:
        """
        limx,limy = self.limites
        partx = int(limx/2)
        x,y=partx,limy-60

        for aminoacido in self.secuencia[:self.limite_aminoacidos]:

            am=Aminoacido(self.screen, aminoacido, (x,y))
            x,y = am.getPosicionActual()
            del am
