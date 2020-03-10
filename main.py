
from random import randint
from app import App

import os


current_directory = os.getcwd()
path_material_virus = current_directory + '/material/virus'
path_material_bacteria = current_directory + '/material/bacteria'

sequences = [os.path.join(path_material_virus, f) for f in os.listdir(path_material_virus)] + [
    os.path.join(path_material_bacteria, f) for f in os.listdir(path_material_bacteria)]

print(sequences)

if __name__ == '__main__':
    a = App()
    a.on_execute()