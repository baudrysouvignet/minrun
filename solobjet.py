import pygame, sys
import os
import random

class sol:
    def __init__(self,x,y,i,image):
        self.x = (x-(i*33))
        self.y = y
        self.image = image
    def afficher_block(self,fenetre):
        self.image = pygame.transform.scale(self.image,(33,33))
        fenetre.blit(self.image,(self.x,self.y))
    def respawn_block(self,image):
        if self.x <=-33:
            self.x= self.x + 838
            self.image = image
