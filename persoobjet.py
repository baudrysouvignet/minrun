import pygame
from pygame.locals import *

class personnage:
    def __init__(self):

        perso = pygame.image.load('src/image/autres/sonic_104_114.png').convert_alpha()
        self.image=[]
        for x in range(0,9*104, 104):
            self.image.append(perso.subsurface(x,0,104,114))
        self.index=0
        self.image_boule=[]
        for x in range(0,8*104, 104):
            self.image_boule.append(perso.subsurface(x,244,104,77)) 

    def affichage_personnage(self,fenetre,index_image,x,y,action):
        if action != "sauter":
            fenetre.blit(self.image[index_image],(x,y))
        else:
            fenetre.blit(self.image_boule[index_image],(x,y))



    def bouge_personnage(self,fenetre):
        self.index = self.index +1
        if self.index == (len(self.image))-1:
            self.index=3

        self.affichage_personnage(fenetre,self.index,400,90,"courrir")


    def saute_sonic(self,fenetre,y):
        if self.index == (len(self.image_boule))-1:
            self.index=0
        else:
            self.index = self.index +1

        self.affichage_personnage(fenetre,self.index,400,y,"sauter")
    
