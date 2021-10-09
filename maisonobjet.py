import pygame, sys
import os
import random

Blocks_images = {"Lila_2":'src/image/Nature/Fleurs/Lila_2.webp',"Lila_1":'src/image/Nature/Fleurs/Lila_1.webp',"Dalle_chene":'src/image/Bois/Chene/Dalle_chene.png',"Porte_2":'src/image/Decoration/Porte_2.webp',"Porte_1":'src/image/Decoration/Porte_1.webp',"Vitre":'src/image/Decoration/Vitre.webp',"Torche":'src/image/Decoration/Torche.webp',"Echelle":'src/image/Decoration/Echelle.webp',"Brick":'src/image/Decoration/Brick.webp',"Beton_orange":'src/image/Decoration/Beton_orange.webp',"Beton_noir":'src/image/Decoration/Beton_noir.webp',"Beton_blanc":'src/image/Decoration/Beton_blanc.webp',"Herbe":'src/image/Nature/Herbe.jpg',"Andesite_blanc":  'src/image/Minerais/Andesite_blanc.jpg',"Andesite":  'src/image/Minerais/Andesite.jpg',"Fer":  'src/image/Minerais/Fer.jpg',"Or":  'src/image/Minerais/Or.jpg',"Stone":  'src/image/Minerais/Stone.jpg',"Planche_bouleau":'src/image/Bois/Bouleau/Planche_bouleau.jpg',"Tronc_bouleau":'src/image/Bois/Bouleau/Tronc_bouleau.jpg',"Planche_chene":'src/image/Bois/Chene/Planche_chene.jpg',"Tronc_chene":'src/image/Bois/Chene/Tronc_chene.jpg',"Planche_chene_sombre":'src/image/Bois/Chene_sombre/Planche_chene_sombre.jpg',"Tronc_chene_sombre":'src/image/Bois/Chene_sombre/Tronc_chene_sombre.jpg'}

class maison:
    def __init__(self,x,y,style):
        self.x = x
        self.y = y
        self.style = style
    def construction(self,fenetre):
        Blocks_images_info = Blocks_images.values()
        Blocks_images_keys = Blocks_images.keys()
        Blocks_images_info = list(Blocks_images_info)

        for i in range(len(Blocks_images_info)):
            Blocks_images_info[i] = pygame.image.load(Blocks_images_info[i]).convert_alpha()
            Blocks_images_info[i] = pygame.transform.scale(Blocks_images_info[i],(30,30))
        
        globale = dict(zip(Blocks_images_keys, Blocks_images_info))

        if self.style == "maison1":
            for w in range(2):
                for i in range(3):
                    fenetre.blit(globale["Tronc_chene"],((self.x+(w*120)),(self.y+(i*30))))
                    fenetre.blit(globale["Echelle"],((self.x+30),(self.y+(i*30))))
                for i in range(3):
                    fenetre.blit(globale["Beton_blanc"],((self.x+30+(w*60)),(self.y+(i*30))))
            for i in range(5):
                fenetre.blit(globale["Dalle_chene"],((self.x+(i*30)),(self.y-30)))
            
            fenetre.blit(globale["Porte_2"],((self.x+60),(self.y+(30))))
            fenetre.blit(globale["Porte_1"],((self.x+60),(self.y+(60))))

            fenetre.blit(globale["Lila_2"],((self.x+150),(self.y+(30))))
            fenetre.blit(globale["Lila_1"],((self.x+150),(self.y+(60))))
            fenetre.blit(globale["Beton_blanc"],((self.x+60),(self.y)))
    def respawn_maison(self,style):
        if self.x <= -180:
            self.x = self.x + 1080
            self.style = style