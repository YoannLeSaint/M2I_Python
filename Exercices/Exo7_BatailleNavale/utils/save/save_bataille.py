import os
from numpy import save, load



def save_current_play(plateau_1, plateau_2, score, path):
    with open(path+'\\plateau_1', 'wb') as f:
        save(f,plateau_1)
    with open(path+'\\plateau_2', 'wb') as f:
        save(f,plateau_2)
    with open(path+'\\score', 'wb') as f:
        save(f,score)

def read_previus_play(path):
    with open(path+'\\plateau_1', 'r') as f:
        plateau_1 = load(f)
    with open(path+'\\plateau_2', 'r') as f:
        plateau_2 = load(f)
    with open(path+'\\score', 'r') as f:
        score = load(f)
    return plateau_1, plateau_2, score


#test
import numpy as np
p1, p2 = np.ones((10,10)), np.ones((10,10))
score = [0,0]
path = "C:\\Users\\lesai\\Mon Drive\\M2I\\05_Python\\Exercices\\Exo7_BatailleNavale"
save_current_play(p1,p2,score,path)


plateau_1, plateau_2, score = read_previus_play(path)