import pygame, sys
from pygame.locals import *

allBullets = pygame.sprite.Group()
allEnemies = pygame.sprite.Group()

initMoney = 300
initScore = 0
initLives = 5
initLevel = 0

gameStats = [initMoney, initLevel, initLives, initScore]

display_width = 1280
display_height = 720

TILESIZE = 40
MAPWIDTH = 32
MAPHEIGHT = 18

GREY = (180, 171, 171)
BROWN = (87, 59, 12)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


PATH = 0
GRASS = 1
START = 2
FINISH = 3
TITLE = 4
SHOP = 5
START = 6
SHOOTER = 7
BOMBER = 8
SNIPER = 9
TOWERS = 10
WIN = 11
SHOOTERSHOP = 12
BOMBERSHOP = 13
SNIPERSHOP = 14
GAMEOVER = 15


colors = {
        PATH: BROWN,
        GRASS: GREEN,
        SHOP: GREY,
        START: BLUE,
        FINISH: RED,
        }


#load images
textures = {
        BOMBER: pygame.image.load('Sprites/Bomber.png'),
        SHOOTER: pygame.image.load('Sprites/Shooter.png'),
        SNIPER: pygame.image.load('Sprites/Sniper.png'),
        #SHOP: pygame.image.load('Sprites/Shop.png'),
        TITLE: pygame.image.load('Sprites/Title.png'),
        START: pygame.image.load('Sprites/Start.png'),
        TOWERS: pygame.image.load('Sprites/Towers.png'),
        WIN: pygame.image.load('Sprites/youWin.gif'),
        SHOOTERSHOP: pygame.image.load('Sprites/ShooterShop.png'),
        BOMBERSHOP: pygame.image.load('Sprites/BomberShop.png'),
        SNIPERSHOP: pygame.image.load('Sprites/SniperShop.png'),
        GAMEOVER: pygame.image.load('Sprites/GameOver.png')
        }


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
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5],
        ]

#pygame.init()

DISPLAYSURF = pygame.display.set_mode((display_width, display_height))


def drawBoard():

        DISPLAYSURF.fill(GREEN)
        
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        if(tilemap[row][column] < 6):
                                #draw tilemap as rectangles in certain colors
                                pygame.draw.rect(DISPLAYSURF, colors[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                                #draw towers
                        if (tilemap[row][column] > 6 and tilemap[row][column] < 10):
                                DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

                        #draw tilemap as images
                        #DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
                                
def drawTowers():
        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        if(tilemap[row][column] == 7 or tilemap[row][column] == 8 or tilemap[row][column] == 9):
                                print("Tadsf")
                                DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

def drawButtons():
         DISPLAYSURF.blit(textures[4], (1050, 20))
         DISPLAYSURF.blit(textures[10], (1050, 70))
         DISPLAYSURF.blit(textures[13], (1050, 120))
         DISPLAYSURF.blit(textures[12], (1050, 200))
         DISPLAYSURF.blit(textures[14], (1050, 280))
         DISPLAYSURF.blit(textures[6], (1050, 650))
         

def getEnemyPath():
        
        enemyPath = [(0,2), (1,2), (1,16), (3,16), (3,1), (22,1), (22,3), (5,3), (5,16), (8,16), (8,6), (22,6), (22,16), (20,16), (20,9), (11,9), (11,12), (17,12), (17,15), (11,15), (11,17), (11,17)]

        return enemyPath

def youWin():
        DISPLAYSURF.blit(textures[11], (350, 220))



