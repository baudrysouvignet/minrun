import pygame, sys
import os
import random

Blocks_images = {"Sable":'src/image/Decoration/sable.png',"Feuillage":'src/image/Decoration/Feuillage.webp',"Barriere_droite_chene":'src/image/Bois/Chene/Barriere_droite_chene.jpeg',"Rose_2":'src/image/Nature/Fleurs/Rose_2.webp',"Rose_1":'src/image/Nature/Fleurs/Rose_1.webp',"Pivoine_2":'src/image/Nature/Fleurs/Pivoine_2.webp',"Pivoine_1":'src/image/Nature/Fleurs/Pivoine_1.webp',"Porte_2_chene_sombre":'src/image/Bois/Chene_sombre/Porte_2_chene_sombre.webp',"Porte_1_chene_sombre":'src/image/Bois/Chene_sombre/Porte_1_chene_sombre.webp',"Porte_1_bouleau":'src/image/Bois/Bouleau/Porte_1_bouleau.webp',"Porte_2_bouleau":'src/image/Bois/Bouleau/Porte_2_bouleau.webp',"Lila_2":'src/image/Nature/Fleurs/Lila_2.webp',"Lila_1":'src/image/Nature/Fleurs/Lila_1.webp',"Dalle_chene":'src/image/Bois/Chene/Dalle_chene.png',"Porte_2_chene":'src/image/Bois/Chene/Porte_2_chene.webp',"Porte_1_chene":'src/image/Bois/Chene/Porte_1_chene.webp',"Vitre":'src/image/Decoration/Vitre.webp',"Torche":'src/image/Decoration/Torche.webp',"Echelle":'src/image/Decoration/Echelle.webp',"Brick":'src/image/Decoration/Brick.webp',"Beton_orange":'src/image/Decoration/Beton_orange.webp',"Beton_noir":'src/image/Decoration/Beton_noir.webp',"Beton_blanc":'src/image/Decoration/Beton_blanc.webp',"Herbe":'src/image/Nature/Herbe.jpg',"Andesite_blanc":  'src/image/Minerais/Andesite_blanc.jpg',"Andesite":  'src/image/Minerais/Andesite.jpg',"Fer":  'src/image/Minerais/Fer.jpg',"Or":  'src/image/Minerais/Or.jpg',"Stone":  'src/image/Minerais/Stone.jpg',"Planche_bouleau":'src/image/Bois/Bouleau/Planche_bouleau.jpg',"Tronc_bouleau":'src/image/Bois/Bouleau/Tronc_bouleau.jpg',"Planche_chene":'src/image/Bois/Chene/Planche_chene.jpg',"Tronc_chene":'src/image/Bois/Chene/Tronc_chene.jpg',"Planche_chene_sombre":'src/image/Bois/Chene_sombre/Planche_chene_sombre.jpg',"Tronc_chene_sombre":'src/image/Bois/Chene_sombre/Tronc_chene_sombre.jpg'}

class maison:
    def __init__(self,x,y,style,materiaux):
        self.x = x
        self.y = y
        self.style = style
        self.materiaux = materiaux
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
                    fenetre.blit(globale[self.materiaux["Bois_tronc"]],((self.x+(w*120)),(self.y+(i*30))))
                    fenetre.blit(globale["Echelle"],((self.x+30),(self.y+(i*30))))
                for i in range(3):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+30+(w*60)),(self.y+(i*30))))
            for i in range(5):
                fenetre.blit(globale["Dalle_chene"],((self.x+(i*30)),(self.y-30)))
            
            fenetre.blit(globale[self.materiaux["Porte_2"]],((self.x+60),(self.y+(30))))
            fenetre.blit(globale[self.materiaux["Porte_1"]],((self.x+60),(self.y+(60))))

            fenetre.blit(globale[self.materiaux["Plante_2"]],((self.x+150),(self.y+(30))))
            fenetre.blit(globale[self.materiaux["Plante_1"]],((self.x+150),(self.y+(60))))
            fenetre.blit(globale[self.materiaux["Beton"]],((self.x+60),(self.y)))
        
        if self.style == "maison2":
            for w in range(2):
                for i in range(6):
                    fenetre.blit(globale[self.materiaux["Bois_tronc"]],((self.x+(w*120)),((self.y-90)+(i*30))))
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(60)),((self.y-90)+(i*30))))
                for i in range(3):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+((i+1)*30)),((self.y)-(w*90))))
                for i in range(2):
                    fenetre.blit(globale["Vitre"],((self.x+(30+w*60)),((self.y-30)+((i-1)*30))))
                    fenetre.blit(globale["Vitre"],((self.x+(90)),((self.y+30)+(i*30))))
                fenetre.blit(globale["Torche"],((self.x+30+(w*60)),((self.y))))
            for i in range(5):
                fenetre.blit(globale["Dalle_chene"],((self.x+(i*30)),(self.y-120)))
            fenetre.blit(globale[self.materiaux["Porte_2"]],((self.x+30),(self.y+(30))))
            fenetre.blit(globale[self.materiaux["Porte_1"]],((self.x+30),(self.y+(60))))
        
        if self.style == "maison3":
            for w in range(2):
                fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(w*90)),((self.y+(w*30)))))
                for i in range(4):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(i*30)),((self.y+60))))
                for i in range(3):
                    fenetre.blit(globale["Vitre"],((self.x+30+((i-w)*30)),((self.y+w*30))))
            for i in range (5):
                fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(i*30)),((self.y-30))))
            for i in range(4):
                fenetre.blit(globale["Feuillage"],((self.x+150),((self.y-30+i*30))))

        if self.style == "maison4":
            for i in range (3):
                fenetre.blit(globale[self.materiaux["Bois_tronc"]],((self.x+60),(self.y+i*30)))
                fenetre.blit(globale["Feuillage"],((self.x+30+i*30),((self.y-30))))
            for i in range (5):
                fenetre.blit(globale["Feuillage"],((self.x+i*30),((self.y))))
            fenetre.blit(globale["Feuillage"],((self.x+60),((self.y-60))))
            fenetre.blit(globale[self.materiaux["Plante_2"]],((self.x+30),(self.y+(30))))
            fenetre.blit(globale[self.materiaux["Plante_1"]],((self.x+30),(self.y+(60))))
        if self.style == "maison5":
             for w in range(4):
                for i in range(6-w*2):
                    fenetre.blit(globale["Sable"],(((self.x+w*30)+i*30),(((self.y+60)-(w*30)))))
        if self.style == "maison6":
            for w in range(2):
                for i in range(6):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(i*30)),((self.y+60+(w*(-60))))))
                    fenetre.blit(globale["Dalle_chene"],((self.x+(i*30)),((self.y-120))))
                for i in range(3):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(i*30)),((self.y-30+(w*(-60))))))
                for i in range(5):
                    fenetre.blit(globale[self.materiaux["Beton"]],((self.x+(w*60)),((self.y-60+i*30))))
                fenetre.blit(globale[self.materiaux["Bois_planche"]],((self.x+150),((self.y-30-(w*30)))))
                fenetre.blit(globale["Vitre"],((self.x+90+w*30),((self.y+30))))
            fenetre.blit(globale["Vitre"],((self.x+30),((self.y+30))))
            fenetre.blit(globale["Vitre"],((self.x+30),((self.y-60))))
            fenetre.blit(globale[self.materiaux["Beton"]],((self.x+150),((self.y+30))))
            for i in range(3):
                fenetre.blit(globale["Feuillage"],((self.x+90+i*30),((self.y-90))))



    def respawn_maison(self,style):
        self.x = self.x + 1080
        self.style = style