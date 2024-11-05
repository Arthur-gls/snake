"""
v1 : pareil mais au moins on peut sortir du programme
avec la touche 'q', ou avec la souris en fermant la fenêtre
"""

from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'

    # les coordonnées de rectangle que l'on dessine
    width = 20 # largeur du rectangle en pixels
    height = 20 # hauteur du rectangle en pixels
    color = (255, 255, 255) # couleur blanche
    for x in range(30):
        if x%2==0:
            for y in range(15):
                x2=x*20
                y2=y*40+20
                rect = pg.Rect(x2, y2, width, height)
                pg.draw.rect(screen, color, rect)
                pg.display.update()
        else:
            for y in range(15):
                x2=x*20
                y2=y*40
                rect = pg.Rect(x2, y2, width, height)
                pg.draw.rect(screen, color, rect)
                pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()