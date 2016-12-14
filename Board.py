import pygame, sys
from pygame.locals import *


display_width = 1280
display_height = 720

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
TITLE = 4
SHOP = 5
START = 6
BOMBER = 7
SHOOTER = 8
SNIPER = 9
TOWERS = 10
WIN = 11




#load images
textures = {
        PATH: pygame.image.load('Sprites/Mud.png'),
        GRASS: pygame.image.load('Sprites/Grass.png'),
        BOMBER: pygame.image.load('Sprites/Bomber.png'),
        SHOOTER: pygame.image.load('Sprites/Shooter.png'),
        SNIPER: pygame.image.load('Sprites/Sniper.png'),
        SHOP: pygame.image.load('Sprites/Shop.png'),
        TITLE: pygame.image.load('Sprites/Title.png'),
        START: pygame.image.load('Sprites/Start.png'),
        TOWERS: pygame.image.load('Sprites/Towers.png'),
        WIN: pygame.image.load('Sprites/youWin.gif')}


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
                [1, 0, 7, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
        ]



pygame.init()

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))


def drawBoard():

        DISPLAYSURF.fill(GREEN)
        
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                                
def drawTowers():
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        if(tilemap[row][column] == 4):
                                DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

def drawButtons():
         DISPLAYSURF.blit(textures[4], (1050, 20))
         DISPLAYSURF.blit(textures[10], (1050, 70))
         DISPLAYSURF.blit(textures[7], (1050, 120))
         DISPLAYSURF.blit(textures[8], (1050, 200))
         DISPLAYSURF.blit(textures[9], (1050, 280))
         DISPLAYSURF.blit(textures[6], (1050, 650))
         

def getEnemyPath():
        enemyPath = [(0,2), (1,2), (1,16), (3,16), (3,1), (22,1), (22,3), (5,3), (5,16), (8,16), (8,6), (22,6), (22,16), (20,16), (20,9), (11,9) (11,12), (17,12), (17,15), (11,15), (11,17)]

        return enemyPath

def youWin():
        DISPLAYSURF.blit(textures[11], (350, 220))

