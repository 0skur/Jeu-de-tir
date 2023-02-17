import pygame
from pygame.locals import *
from math import *
from random import randint

balle_rayon=20
(largeur, hauteur) = (800, 600)
listeBalle = []
balle = []
class balles:
    src = pygame.image.load("balle.png")
    x = randint(balle_rayon, largeur-balle_rayon)
    y = 95
    balle_vitesseX=5
    balle_vitesseY=2
    def nouvelleBalle(self, src, y, balle_vitesseX, balle_vitesseY):
        x = randint(balle_rayon, largeur-balle_rayon)
        balle = []
        balle.append(src)
        balle.append(x)
        balle.append(y)
        balle.append(balle_vitesseX)
        balle.append(balle_vitesseY)
        listeBalle.append(balle)

balles = balles()

balle.append(balles.src)
balle.append(balles.x)
balle.append(balles.y)
balle.append(balles.balle_vitesseX)
balle.append(balles.balle_vitesseY)
listeBalle.append(balle)
balle = []