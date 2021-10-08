import pygame, sys
import os
import random

Blocks_images = {"Herbe":'src/image/Nature/Herbe.jpg',"Andesite_blanc":  'src/image/Minerais/Andesite_blanc.jpg',"Andesite":  'src/image/Minerais/Andesite.jpg',"Fer":  'src/image/Minerais/Fer.jpg',"Or":  'src/image/Minerais/Or.jpg',"Stone":  'src/image/Minerais/Stone.jpg',"Planche_bouleau":'src/image/Bois/Bouleau/Planche_bouleau.jpg',"Tronc_bouleau":'src/image/Bois/Bouleau/Tronc_bouleau.jpg',"Planche_chene":'src/image/Bois/Chene/Planche_chene.jpg',"Tronc_chene":'src/image/Bois/Chene/Tronc_chene.jpg',"Planche_chene_sombre":'src/image/Bois/Chene_sombre/Planche_chene_sombre.jpg',"Tronc_chene_sombre":'src/image/Bois/Chene_sombre/Tronc_chene_sombre.jpg'}

class maison:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def construction(self,style,fenetre):
        Blocks_images_info = Blocks_images.values()
        Blocks_images_keys = Blocks_images.keys()
        Blocks_images_info = list(Blocks_images_info)

        for i in range(len(Blocks_images_info)):
            Blocks_images_info[i] = pygame.image.load(Blocks_images_info[i])
            Blocks_images_info[i] = pygame.transform.scale(Blocks_images_info[i],(30,30))
        
        globale = dict(zip(Blocks_images_keys, Blocks_images_info))

        if style == "maison1":
            for w in range(2):
                for i in range(3):
                    fenetre.blit(globale["Tronc_chene_sombre"],((590+(6*w*30)),(170-(i*30))))
            for w in range(2):
                for i in range(2):
                    fenetre.blit(globale["Planche_chene_sombre"],((620+(4*w*30)),(170-((2*i)*30))))
                    fenetre.blit(globale["Tronc_chene_sombre"],((620+(4*w*30)),(170-30)))
            for w in range(2):
                for i in range(3):
                    fenetre.blit(globale["Planche_chene_sombre"],((650+(2*w*30)),(170-(i*30))))
            
            fenetre.blit(globale["Planche_chene_sombre"],((680),(110)))