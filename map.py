import pygame, sys
from pygame.locals import *


TILESIZE = 50
MAPWIDTH = 10
MAPHEIGHT = 10

GRAY = (87, 59, 12)
GREEN = (34, 139, 34)


PATH = 0
GRASS = 1


#textures = {PATH : pygame.image.load('tile.png'), GRASS : pygame.image.load('grass.png')}
colours = {PATH : GRAY, GRASS : GREEN}

enemyPath = [(2,0), (2,0), (2,0), (2,0), (2,0)]


tilemap = [
                [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
                [GRASS, GRASS, GRASS, PATH, PATH, PATH, PATH, GRASS, GRASS, GRASS],
                [PATH, PATH, GRASS, PATH, GRASS, GRASS, PATH, GRASS, GRASS, GRASS],
                [GRASS, PATH, GRASS, PATH, GRASS, GRASS, PATH, GRASS, GRASS, GRASS],
                [GRASS, PATH, GRASS, PATH, GRASS, PATH, PATH, GRASS, GRASS, GRASS],
                [PATH, PATH, GRASS, PATH, GRASS, PATH, GRASS, GRASS, GRASS, GRASS],
                [PATH, GRASS, GRASS, PATH, GRASS, PATH, GRASS, GRASS, GRASS, GRASS],
                [PATH, GRASS, GRASS, PATH, GRASS, PATH, GRASS, PATH, PATH, PATH],
                [PATH, PATH, PATH, PATH, GRASS, PATH, GRASS, PATH, GRASS, GRASS],
                [GRASS, GRASS, GRASS, GRASS, GRASS, PATH, PATH, PATH, GRASS, GRASS],
        ]


pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

while True:

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        for row in range(MAPHEIGHT):
                for column in range(MAPWIDTH):
                        #images/textures
                        #DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

                        #colours
                        pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

        pygame.display.update()

        
