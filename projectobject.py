import pygame, sys
from pygame.locals import *
import os
import random
from solobjet import *
from maisonobjet import *


def affichage_rue():
    pygame.draw.rect(window, (192,192,192),(0, 200, WIDTH, HEIGHT//2),0)
pygame.init()

WIDTH = 800
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Balade en ville')
CIEL = (135,206,235)
avancer = 0

bouger=0
vel = 5

h=200
sol_images = [pygame.image.load('src/image/Minerais/Andesite_blanc.jpg') ,pygame.image.load('src/image/Minerais/Andesite.jpg') ,pygame.image.load('src/image/Minerais/Fer.jpg') ,pygame.image.load('src/image/Minerais/Or.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ]
def image():
    if h == 200:
        image = pygame.image.load('src/image/Nature/Herbe.jpg') 
    else:
        image= random.choice(sol_images)
    return image
imageh = pygame.image.load('src/image/Nature/Herbe.jpg') 


sol_block =[]
for i in range (4):
    for i in range (26):
        if h==200:
            sol_block.append(i)
            sol_block[i] = sol(800,h,i,image())
        elif h==233:
            sol_block.append(i+27)
            sol_block[i+26] = sol(800,h,i,image())
        elif h==266:
            sol_block.append(i+54)
            sol_block[i+52] = sol(800,h,i,image())
    h = h+33
print(sol_block[25].x)
maison1 = maison(620,0)
continuer=1
while continuer:
    window.fill(CIEL)
    affichage_rue()
    for event in pygame.event.get():
        if event.type==QUIT: 
            continuer=0
    for i in range (26):
        sol_block[i].afficher_block(window)
        sol_block[i+26].afficher_block(window)
        sol_block[i+52].afficher_block(window)
    
    maison1.construction("maison1",window)



    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                bouger=1
            if event.key == K_UP:
                sauter=1/"b"
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                bouger=0
    if bouger == 1:
        for i in range(78):
            sol_block[i].x = int(sol_block[i].x)-vel
            if sol_block[i].y==200:
                sol_block[i].respawn_block(imageh)
            else:
                sol_block[i].respawn_block(image())
    pygame.display.flip()


