import pygame, sys
from pygame.locals import *


display_width = 1280
display_height = 720

#40 * 15 = 600

TILESIZE = 40
MAPWIDTH = 32
MAPHEIGHT = 18


GRAY = (87, 59, 12)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
RED = (255, 0 , 0)


PATH = 0
GRASS = 1
START = 2
FINISH = 3
BOMBER = 4
SHOP = 5
TITLE = 6
START = 7


#load images
textures = {
        PATH: pygame.image.load('Sprites/Mud.png'),
        GRASS: pygame.image.load('Sprites/Grass.png'),
        BOMBER: pygame.image.load('Sprites/Bomber.png'),
        SHOP: pygame.image.load('Sprites/Shop.png'),
        TITLE: pygame.image.load('Sprites/Title.png'),
        START: pygame.image.load('Sprites/Start.png')}


#colours = {PATH: GRAY, GRASS: GREEN, START: BLUE, FINISH: RED}


tilemap = [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 4, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
        ]



pygame.init()

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))


def drawBoard():

        DISPLAYSURF.fill(GREEN)
        
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):

                        #scale(Surface, (width, height)
                        #images/textures
                        DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

                        #colours
##                        if(tilemap[row][column] < 4):
##                                pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
##
##                        
##                        elif(tilemap[row][column] > 6):
##                                pygame.draw.rect(DISPLAYSURF, GREEN, (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))
##
                                
def drawTowers():
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        if(tilemap[row][column] == 4):
                                #a.topleft = ((row * 50 + 40), (column * 40 + 40))
                                #DISPLAYSURF.blit(Bomber, (row, column))
                                DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

def drawButtons():
         DISPLAYSURF.blit(textures[6], (1050, 20))
         DISPLAYSURF.blit(textures[7], (1050, 650))

def getEnemyPath():
        
        enemyPath = [(0,2), (1,2), (1,16), (3,16), (3,1), (22,1), (22,3), (5,3), (5,16), (8,16), (8,6), (22,6), (22,16), (20,16), (20,9), (11,9) (11,12), (17,12), (17,15), (11,15), (11,17)]

        return enemyPath

        
##        path = []
##        for row in range(MAPHEIGHT):
##                for column in range(MAPWIDTH):
##                        if((tilemap[row][column]) == 0):
##                                
##                                path.append((row, col))


##while True:
##
##        for event in pygame.event.get():
##                if event.type == QUIT:
##                        pygame.quit()
##                        sys.exit()
##
##        drawBoard()
##
##        drawTowers()
##
##                        
##
##                        
##        
##
##        pygame.display.update()

        
