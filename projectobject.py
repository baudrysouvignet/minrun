import pygame, sys
from pygame.locals import *
import os
import random
from solobjet import *
from maisonobjet import *
from persoobjet import *



def affichage_rue():
    pygame.draw.rect(window, (192,192,192),(0, 200, WIDTH, HEIGHT//2),0)
pygame.init()



WIDTH = 800
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('MinRun')
CIEL = (135,206,235)
avancer = 0
sauter = 0
bouger=0
vel = 8

h=200
sol_images = [pygame.image.load('src/image/Minerais/Andesite_blanc.jpg') ,pygame.image.load('src/image/Minerais/Andesite.jpg') ,pygame.image.load('src/image/Minerais/Fer.jpg') ,pygame.image.load('src/image/Minerais/Or.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ,pygame.image.load('src/image/Minerais/Stone.jpg') ]

sonic = personnage()
def image():
    if h == 200:
        image = pygame.image.load('src/image/Nature/Herbe.jpg') 
    else:
        image= random.choice(sol_images)
    return image
i=0
m = ""
maison_type = ""
def maison_choix():
    global m, maison_type
    while m == maison_type:
        maison_type = ["maison1","maison2","maison3","maison4","maison5","maison6"]
        maison_type = random.choice(maison_type)
    m = maison_type
    return maison_type
imageh = pygame.image.load('src/image/Nature/Herbe.jpg') 


materiaux_choix = {}
# Block aleatoirs
boiss = ""
bois = "c"
bettonn =""
betton = "b"
plantee = ""
plante ="p"
def materiaux():
    global boiss, bois, bettonn, betton, plantee, plante
    while boiss ==  bois:
        bois = ["chene","bouleau","chene_sombre"]
        bois = random.choice(bois)
    boiss = bois
    if bois == "chene":
        materiaux_choix["Bois_tronc"] = "Tronc_chene"
        materiaux_choix["Bois_planche"] = "Planche_chene"
        materiaux_choix["Porte_1"] = "Porte_1_chene"
        materiaux_choix["Porte_2"] = "Porte_2_chene"
        materiaux_choix["Bois_barriere"] = "Barriere_droite_chene"
    elif bois == "bouleau":
        materiaux_choix["Bois_tronc"] = "Tronc_bouleau"
        materiaux_choix["Bois_planche"] = "Planche_bouleau"
        materiaux_choix["Porte_1"] = "Porte_1_bouleau"
        materiaux_choix["Porte_2"] = "Porte_2_bouleau"
        materiaux_choix["Bois_barriere"] = "Barriere_droite_chene"
    else:
        materiaux_choix["Bois_tronc"] = "Tronc_chene_sombre"
        materiaux_choix["Bois_planche"] = "Planche_chene_sombre"
        materiaux_choix["Porte_1"] = "Porte_1_chene_sombre"
        materiaux_choix["Porte_2"] = "Porte_2_chene_sombre"
        materiaux_choix["Bois_barriere"] = "Barriere_droite_chene"
    
    while bettonn == betton:
        betton = ["noir","orange","blanc"]
        betton = random.choice(betton)
    bettonn = betton
    if betton == "noir":
        materiaux_choix["Beton"] = "Beton_noir"
    elif betton == "orange":
        materiaux_choix["Beton"] = "Beton_orange"
    else:
        materiaux_choix["Beton"] = "Beton_blanc"
    
    while plantee == plante:
        plante = ["lila","pivoine","rose"]
        plante = random.choice(plante)
    plantee = plante
    if plante == "lila":
        materiaux_choix["Plante_1"] = "Lila_1"
        materiaux_choix["Plante_2"] = "Lila_2"
    elif plante == "pivoine":
        materiaux_choix["Plante_1"] = "Pivoine_1"
        materiaux_choix["Plante_2"] = "Pivoine_2"
    else:
        materiaux_choix["Plante_1"] = "Rose_1"
        materiaux_choix["Plante_2"] = "Rose_2"
    
    return materiaux_choix

    

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
    
maison_info = []
for i in range(6):
    maison_info.append(i)
    maison_info[i] = maison(800-(180*i),110,maison_choix(),materiaux())
    materiaux_choix = {}
    
distence = 0
distencevaleur = 0
arial = pygame.font.SysFont("Arial", 15, bold=True, italic=False)
fontgg = pygame.font.SysFont("Arial", 100, bold=True, italic=False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scorepoint = "Distence: "+str(distence)+"m"
    score = arial.render(str(scorepoint),False,(0,0,0))
    if distencevaleur == 100:
        if vel <= 31:
            vel = vel + 3
            distencevaleur = distencevaleur-100
            multiplica = multiplica+1
            
        else:
            distencevaleur = distencevaleur-100
    if distence >= 1000 and distence <= 1030:
        gg = fontgg.render(str("1000"),False,(255,215,0))
        window.blit(gg,(230,80))
    window.fill(CIEL)
    affichage_rue()
    for i in range (26):
        sol_block[i].afficher_block(window)
        sol_block[i+26].afficher_block(window)
        sol_block[i+52].afficher_block(window)
    
    for i in range(len(maison_info)):
        maison_info[i].construction(window)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                bouger=1
            if event.key == K_LEFT:
                running = False
            if event.key == K_UP:
                sauter=1
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                bouger=0
            if event.key == K_UP:
                sauter=0
    if bouger==1 and sauter==1:
        personnage.saute_sonic(sonic,window,50)
    if bouger==0 and sauter==1:
        personnage.saute_sonic(sonic,window,50)
    if bouger==1 and sauter==0:
        personnage.bouge_personnage(sonic,window)
    if bouger==0 and sauter==0:
        personnage.affichage_personnage(sonic,window,0,400,90,"rien")
    if bouger == 1:
        distence = round((distence+0.3),1)
        distencevaleur = distencevaleur+0.3
        for i in range(len(maison_info)):
            maison_info[i].x = maison_info[i].x-(vel-1)
            if maison_info[i].x <= -180:
                maison_info[i].respawn_maison(maison_choix())
        for i in range(78):
            sol_block[i].x = int(sol_block[i].x)-vel
            if sol_block[i].y==200:
                sol_block[i].respawn_block(imageh)
            else:
                sol_block[i].respawn_block(image())
    window.blit(score,(10,10))
    pygame.display.flip()
