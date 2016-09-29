import pygame, sys
from pygame.locals import *
import random

z=[]
y=[]
q=[]
num=4
matrix = [[0 for i in range(num)] for j in range(num)]

def solveMaze(Maze,pos,N):
    retval=[]
    if pos==(N-1,N-1):
        retval=[(N-1,N - 1)]
        return retval
    x , y = pos
    if x + 1< N and Maze[x+1][y]==1:
        a = solveMaze(Maze, (x + 1, y), N)
        if a!= None:
            retval=[(x , y )] + a
            return retval

    if y + 1 < N and Maze[x][y+1] == 1:
        b = solveMaze( Maze , (x , y + 1) , N )
        if  b != None:
            retval = [( x,y)] + b
            return retval

def main():

    pygame.init()
    # pygame.font.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    blue=(0,0,255)
    red=(255,0,0)
    green=(0,255,0)
    black= (0,0,0)
    color=[WHITE,black]
    rand_colours =[random.choice(color) for i in range(2)]
    DISPLAY.fill(green)

    # basicfont = pygame.font.SysFont(None, 48)
    # text = basicfont.render('Hello World!', True, (255, 0, 0), (255, 255, 255))
    # DISPLAY.blit(text, (10, 100))
    perc=60
    for j in range(num):
        for i in range(num):
            x = random.randint(1,100)
            col=black
            if(x>perc):
                col=WHITE
            pygame.draw.rect(DISPLAY, col, (10+70*i, 100+70*j, 50, 50))

    pygame.draw.rect(DISPLAY, red, (10, 100, 50, 50))
    pygame.draw.rect(DISPLAY, blue, (10+70*(num-1), 100+70*(num-1), 50, 50))

    for j in range(num):
        for i in range(num):
            z.append(DISPLAY.get_at((10 + 70 * i+1, 100 + 70 * j+1)))

    final_list=[]
    y=[]
    for x in z:
        for i in x[:3]:
            y.append(i/255)
            if len(y)==3:
                q.append(y)
                y=[]
    print len(matrix)
    for j in range(num):
        for i in range(num):
            matrix[j][i]=q[j*num+i]

    for j in matrix:
        for h in j:
            if sum(h)<3:
                final_list.append(1)
            else:
                final_list.append(0)


    final_matrix= [final_list[x:x + num] for x in xrange(0, len(final_list), num)]
    print final_matrix
    anslist=solveMaze(final_matrix, (0, 0), num)

    if anslist is not None:
        for x in anslist:
            a,b= x
            a,b= x
            pygame.draw.rect(DISPLAY, blue, (10 + 70 * a, 100 + 70 * b, 50, 50))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()