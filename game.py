import pygame
import time
from Tower import *
from Enemy import *
from Board import *

pygame.init()
pygame.font.init()

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
def introMenu():
        #list of menu text
        text = ['Play Game', 'Quit']
        run = True
        bg = pygame.image.load("harambe.png")
        
        pygame.mixer.music.load("menu.mp3")
        pygame.mixer.music.play(-1)
        while run:
                mouseClicked = False
                screen.blit(bg, (0,0))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        elif event.type == pygame.MOUSEBUTTONUP:
                                mouseClicked = True
                                
                font = pygame.font.Font('Fonts/freesansbold.ttf',30)
                x = display_width/2
                y = display_height/2
                #isClick = stores location of menu items "rect"
                isClick = []
                
                # writes menu text, diff col if mouseover
                for t in text:
                        tex = font.render(t, True, black)
                        texR = tex.get_rect()
                        texR.center = (x,y)
                        if texR.collidepoint(pygame.mouse.get_pos()):
                                tex = font.render(t, True, red)
                        screen.blit(tex, texR)
                        y += 35
                        isClick.append(texR)
                #clickable menu items
                if mouseClicked and isClick[0].collidepoint(event.pos):
                        theGame()
                if mouseClicked and isClick[1].collidepoint(event.pos):
                        pygame.quit()
                        quit()
                                
                pygame.display.update()
                clock.tick(15)
        
def theGame():
        #Initialize mouse and screen
        pygame.mixer.music.stop()
        screen.fill(black)
        mousex = 0
        mousey = 0
        selectedTower = None
        mouseClicked = False
        #Initialize game
        money = 200
        score = 0
        lives = 5
        level = 0
        run = True

        red = Red(40)
        
        allSprites = pygame.sprite.Group()
        allSprites.add(red)
        
        while run:
                drawBoard()
                drawButtons()
                
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        elif event.type == pygame.MOUSEMOTION:
                                mousex, mousey = event.pos
                        elif event.type == pygame.MOUSEBUTTONUP:
                                mousex, mousey = event.pos
                                mouseClicked = True
                if 1 == 3:
                        youWin()
                if mouseClicked:
                        whatClicked = click(mousex, mousey, level)
                        if whatClicked == 'placeSh':
                                placeTower(8)
                        if whatClicked == 'placeB':
                                placeTower(7)
                        if whatClicked == 'placeSn':
                                placeTower(9)
                allSprites.update()
                allSprites.draw(screen)
                pygame.display.flip()
                clock.tick(30)

def click(mousex, mousey, level):
	if mousex >= 1050 and mousex <= 1090 and mousey >= 120 and mousey <= 160:
		return 'placeSh'
	elif mousex >= 1050 and mousex <= 1090 and mousey >= 200 and mousey <= 240:
		return 'placeB'
	elif mousex >= 1050 and mousex <= 1090 and mousey >= 280 and mousey <= 320:
		return 'placeSn'
	elif mousex >= 1050 and mousex <= 1230 and mousey >= 650 and mousey <= 710:
		return 'start'
	else:
		return None

##def startWave(level):
        
        
def placeTower(tower):
        mouseClick = False
        runIt = True
        while runIt:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        elif event.type == pygame.MOUSEMOTION:
                                mousex, mousey = event.pos
                        elif event.type == pygame.MOUSEBUTTONUP:
                                mousex, mousey = event.pos
                                mouseClick = True
                if mouseClick == True:
                        x, y = getGridAtPixel(mousex, mousey)
                        x1 = int(x)
                        y1 = int(y)
                        if tilemap[y1][x1] == 1:
                                tilemap[y1][x1] = tower
                                runIt = False
        
def getGridAtPixel(mousex, mousey):
	x = (mousex) / 40
	y = (mousey) / 40
	if x >= 0 and x <= 25 and y >= 0 and y <= 18:
		return x, y
	
                
introMenu()
pygame.quit()
quit()
