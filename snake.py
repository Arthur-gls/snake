from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((240, 420))
clock = pg.time.Clock()

# CONSTANTES

width = 20 # largeur du rectangle en pixels
height = 20 # hauteur du rectangle en pixels
white = (255, 255, 255) # couleur blanche
red=(255,0,0)
blue=(85,156,255)
green1=(0,255,0)
green2=(0,200,0)
black=(0,0,0)
snake = [(4, 11),(3, 11),(2, 11)]
head=snake[0]
apple=False
score=0
direction=(1,0)
l,L=12,21
size=20

def first_fruit(l,L):
    apple_x,apple_y=randint(0,l-1),randint(0,L-1)
    return apple_x,apple_y


def act_event(event,direction,snake,action):
    running=True
    # chaque évênement à un type qui décrit la nature de l'évênement
    # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
    if event.type == pg.QUIT:
        running = False
    # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            if direction!=(-1,0):
                direction=(1,0)
                snake.pop()
                x,y=snake[0][0],snake[0][1]
                new_cell=[(x+direction[0],y+direction[1])]
                snake=new_cell+snake
                action=True
        if event.key == pg.K_LEFT:
            if direction!=(1,0):
                direction=(-1,0)
                snake.pop()
                x,y=snake[0][0],snake[0][1]
                new_cell=[(x+direction[0],y+direction[1])]
                snake=new_cell+snake
                action=True
        if event.key == pg.K_UP:
            if direction!=(0,1):
                direction=(0,-1)
                snake.pop()
                x,y=snake[0][0],snake[0][1]
                new_cell=[(x+direction[0],y+direction[1])]
                snake=new_cell+snake
                action=True
        if event.key == pg.K_DOWN:
            if direction!=(0,-1):
                direction=(0,1)
                snake.pop()
                x,y=snake[0][0],snake[0][1]
                new_cell=[(x+direction[0],y+direction[1])]
                snake=new_cell+snake
                action=True
        if event.key == pg.K_q:
            running = False
    return running,direction,snake,action

def damier(w,h,color,size,l,L):
    for x in range(l):
        if x%2==0:
            for y in range(L//2+1):
                x2=x*size
                y2=y*size*2
                rect = pg.Rect(x2, y2, w, h)
                pg.draw.rect(screen, color, rect)
        else:
            for y in range(L//2+1):
                x2=x*size
                y2=y*size*2+size
                rect = pg.Rect(x2, y2, w, h)
                pg.draw.rect(screen, color, rect)

def fruit(apple,color,size,width,height,snake,l,L,apple_x,apple_y):
    # on place la pomme

    if apple:
        rect=pg.Rect(apple_x*size,apple_y*size,width,height)
        pg.draw.rect(screen,red,rect)
        apple=True

    # s'il n'y a plus de pomme on en fait spawn une

    if not apple:
        apple_x,apple_y=snake[-1]
        while (apple_x,apple_y) in snake:

            apple_x,apple_y=randint(0,l-1),randint(0,L-1)
        
        rect=pg.Rect(apple_x*size,apple_y*size,width,height)
        pg.draw.rect(screen,red,rect)
        apple=True
    return apple,apple_x,apple_y

def growth(snake,apple_x,apple_y,score,head,apple):
    if head==(apple_x,apple_y):
        score+=1
        apple=False
        tail_direction=(snake[-1][0]-snake[-2][0],snake[-1][1]-snake[-2][1])
        new_cell2=[(snake[-1][0]+tail_direction[0],snake[-1][1]+tail_direction[1])]
        snake=snake+new_cell2
    return snake,score,apple

def act_snake(snake,action,direction,width,height,size,color):
    if not action:
        snake.pop()
        x,y=snake[0][0],snake[0][1]
        new_cell=[(x+direction[0],y+direction[1])]
        snake=new_cell+snake

    for k in snake:
        x=k[0]*size
        y=k[1]*size
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, blue,rect)
    return snake

def L_condition(snake,running):
    head=snake[0]
    if head in snake[1::]:
        running=False

    if head[0]>=l or head[1]>=L or head[0]<0 or head[1]<0:
        running=False
    return running

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
apple_x,apple_y=first_fruit(l,L)

while running:
    screen.fill(green1)
    clock.tick(5)
    action=False

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant 0.2 seconde précédente

    for event in pg.event.get():
        running,direction,snake,action=act_event(event,direction,snake,action)

    # on construit le damier

    damier(width,height,green2,size,l,L)

    # on place la pomme

    apple,apple_x,apple_y=fruit(apple,red,size,width,height,snake,l,L,apple_x,apple_y)

    # si l'utilisateur mange la pomme il grossit

    snake,score,apple=growth(snake,apple_x,apple_y,score,head,apple)

    # on dessine le serpent et on le fait bouger

    snake=act_snake(snake,action,direction,width,height,size,blue)

    # on perd si on se mange la queue ou si on sort de l'arène

    head=snake[0]
    running=L_condition(snake,running)

    pg.display.update()

    # on actualise le score

    score_msg='Score = ' +str(score)
    pg.display.set_caption(score_msg)


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows

pg.quit()