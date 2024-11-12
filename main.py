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
snake = [(10,15),(11,15),(12,15)]
direction = (1,0)
running = True

pomme=(5,5)

while running:

    clock.tick(20)

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
            elif event.key == pg.K_RIGHT and direction != (-1,0):
                direction = (1,0)
            elif event.key == pg.K_LEFT and direction != (1,0):
                direction = (-1,0)
            elif event.key == pg.K_UP and direction != (0,1):
                direction = (0,-1)
            elif event.key == pg.K_DOWN and direction != (0,-1):
                direction = (0,1)

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...
    screen.fill((0,0,0))


 #   for i in range (30):
#        for j in range (30):
 #           if (i+j)%2==0 : 
  #              x=i*20
   #             y=j*20
    #            width=20
     #           height=20
      #          rect=pg.Rect(x, y, width, height)
       #         pg.draw.rect(screen, (255,255,255), rect)

    
    for z in snake:
        x=z[0]*20
        y=z[1]*20
        width=20
        height=20
        rect=pg.Rect(x, y, width, height)
        pg.draw.rect(screen, (255,0,0), rect)
        
    x=pomme[0]*20
    y=pomme[1]*20
    width=20
    height=20
    rect=pg.Rect(x, y, width, height)
    pg.draw.rect(screen, (0,255,0), rect)

    if (snake[-1][0]+direction[0],snake[-1][1]+direction[1])==pomme : 
        snake=snake+[(snake[-1][0]+direction[0],snake[-1][1]+direction[1])]
        pomme=(randint(0,29),randint(0,29))
        print (pomme)
    else : 
        snake=snake[1:]+[(snake[-1][0]+direction[0],snake[-1][1]+direction[1])]

    for i in range(len(snake)):
        snake[i]=(snake[i][0]%30,snake[i][1]%30)

    
    


    






    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()
