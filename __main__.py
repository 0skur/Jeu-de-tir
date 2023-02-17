"""
Jeu_Tir en python avec biblio Pygame
Ressources: https://www.pygame.org/docs/
https://riptutorial.com/fr/pygame/topic/3959/commencer-avec-pygame
F HERGNIOT amélioré par axel TEILLET
"""
#Importation des bibliothèques nécessaires
import pygame
from balles import *
from pygame.locals import *
from math import *
from random import randint
# Initialisation des variables
(largeur, hauteur) = (800, 600)  # definit la hauteur et la largeur de la fenêtre de l'application
WHITE=(225, 225, 225)   #couleur blanche
RED=(0,0,0)   #couleur rouge
gris = (200 ,200, 200)
missile_x=200   #coordonées x du missile
screen = pygame.display.set_mode((largeur, hauteur))

balleLargeur= 40   #rayon de la balle
balle_vitesseX=5   #vitesse x de la balle
balle_vitesseY=2   #vitesse y de la balle
vitesseMissile=10
FPS = 60    #FPS
gagne=0
perdu=0


src = pygame.image.load("balle.png")
x = randint(balleLargeur, largeur-balleLargeur)
y = 95

#Initialisation de la bibliothèque Pygame
pygame.init()
clock = pygame.time.Clock()  # créer un système permettant de gérer le temps

fenetre = pygame.display.set_mode((largeur, hauteur), RESIZABLE) #Création de la fenêtre redimensionnable
fenetre.fill(WHITE) 
missile = pygame.image.load("missile2.png").convert_alpha()  #Chargement image en rendant le blanc de l'image transparent
flecheHaut = pygame.image.load("flecheHaut.png")
flecheBas = pygame.image.load("flecheBas.png")
missile_y=hauteur-missile.get_height() #coordonées y du missile

#BOUCLE INFINIE
continuer = True
tir = False
collision = False
while continuer:
    nombreBalleCalc = len(listeBalle)
    clock.tick(FPS)   #Précise le nombre d'image par seconde Frame par seconde
    
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False 
        if event.type == MOUSEBUTTONDOWN:
            for i in range(0, len(listeBalle)):
                if event.pos[0] >= 600 and event.pos[0] <= 615 and event.pos[1] >= 40 and event.pos[1] <= 60:
                    if abs(listeBalle[i][3]*0.95) > 1 and abs(listeBalle[i][4]*0.95) > 1:
                        listeBalle[i][3]*=0.95
                        listeBalle[i][4]*=0.95
                        vitesseMissile*=0.95
                elif event.pos[0] >= 730 and event.pos[0] <= 745 and event.pos[1] >= 40 and event.pos[1] <= 60:
                    listeBalle[i][3]*=1.05
                    listeBalle[i][4]*=1.05
                    vitesseMissile*=1.05
                elif event.pos[0] >= 495 and event.pos[0] <= 537 and event.pos[1] >= 7 and event.pos[1] <= 20:
                    if listeBalle[i][3] < 0:
                        listeBalle[i][3]=-5
                    else:
                        listeBalle[i][3]=5
                        listeBalle[i][4]=2
                        vitesseMissile=10
                        gagne=0
                        perdu=0
                        listeBalle[i][1]=randint(0+balleLargeur, largeur-balleLargeur)
                        listeBalle[i][2]=balleLargeur+75 
        if event.type == KEYDOWN :  # Si touche appuyée
            if event.key == K_UP and tir == False:   #rôle:déplacement vers la droite
                tir = True

            if event.key == K_d:
                balles.nouvelleBalle(src, y, balle_vitesseX, balle_vitesseY)
    k = pygame.key.get_pressed()
    if k[pygame.K_RIGHT] and not(tir) and missile_x<largeur-30:
        missile_x+=7.5
    if k[pygame.K_LEFT] and not(tir) and missile_x>30:
        missile_x-=7.5
            
    
    fenetre.fill(WHITE)  # couleur de la fenetre
    # pygame.draw.circle(fenetre, RED, (balles.listeBalle.x, balles.listeBalle.y), balleLargeur)  # tracé d'un cercle
    pygame.draw.rect(screen, gris, (0, 0, 800, 75))

    font_obj = pygame.font.Font('freesansbold.ttf', 12)  # police d'écriture
    gagneText = font_obj.render('Gagne: ', True, RED, gris)  # couleur du texte
    gagneTextScore = font_obj.render(str(gagne), True, RED, gris)
    perduText = font_obj.render("Perdu: ", True, RED, gris)
    perduTextScore = font_obj.render(str(perdu),True, RED, gris)

    resetText = font_obj.render("Reset", True, RED, gris)
    vitessePText = font_obj.render('Augmenter vitesse', True, RED, gris)
    vitesseMText = font_obj.render('Diminuer vitesse', True, RED, gris)
    nombreBalleText = font_obj.render("Nombre de balle :", True, RED, gris)
    nombreBalle = font_obj.render(str(nombreBalleCalc), True, RED, gris)

    if tir:
        missile_y=missile_y-vitesseMissile
    for i in range(0,len(listeBalle)):
        
        print("vitesseX:", listeBalle[0][3], "vitesseY:", listeBalle[0][4])
        

        fenetre.blit(listeBalle[i][0], (listeBalle[i][1], listeBalle[i][2]))
        listeBalle[i][2] += 1

        listeBalle[i][1] = listeBalle[i][1] + listeBalle[i][3]  # rôle:

        if listeBalle[i][1] + balleLargeur >= largeur:
            listeBalle[i][3] = -listeBalle[i][3]

        if listeBalle[i][1] <= 0:
            listeBalle[i][3] = -listeBalle[i][3]

        if listeBalle[i][2] == hauteur - 100:
            listeBalle[i][2] = balleLargeur+75
            perdu+=1

        if tir:
            
            if abs(missile_x - listeBalle[i][1]) < 25 and abs(missile_y - listeBalle[i][2]) < 25:
                collision = True
            if missile_y < 50:
                missile_y = hauteur-missile.get_height()
                tir = False
            
        if collision:
            collision = False
            tir = False
            listeBalle[i][2] = balleLargeur+50
            missile_y = hauteur-missile.get_height()
            gagne=gagne+1

    fenetre.blit(gagneText, (10, 10))
    fenetre.blit(gagneTextScore, (60, 10))
    fenetre.blit(perduText, (90, 10))
    fenetre.blit(perduTextScore, (150, 10))
    fenetre.blit(missile, (missile_x, missile_y))
    fenetre.blit(vitessePText, (largeur-120, 10))
    fenetre.blit(flecheHaut, (largeur-70, 40))
    fenetre.blit(vitesseMText, (largeur-240, 10))
    fenetre.blit(flecheBas, (largeur-200, 40))
    fenetre.blit(resetText, (largeur-300, 10))
    fenetre.blit(nombreBalle, (largeur-540, 10))
    fenetre.blit(nombreBalleText, (largeur-650, 10))

    pygame.display.flip()  # Rafraîchissement de l'écran

pygame.quit()