import pygame
import time
from Tower import *
from Enemy import *
from Map import *
pygame.init()

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
                                
                font = pygame.font.Font('freesansbold.ttf',30)
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
        
        run = True
        x,y = 0,2
        x *= 40
        y *= 40

        block = Block(black, 30,30)
        
        blockList = pygame.sprite.Group()
        allSprites = pygame.sprite.Group()
        block.rect.x = x
        block.rect.y = y
        blockList.add(block)
        allSprites.add(block)
        
        while run:
                drawBoard()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        elif event.type == pygame.MOUSEMOTION:
                                mousex, mousey = event.pos
                        elif event.type == pygame.MOUSEBUTTONUP:
                                mousex, mousey = event.pos
                                mouseClicked = True
                allSprites.update()
                allSprites.draw(screen)
                pygame.display.flip()
                clock.tick(30)
                
introMenu()
pygame.quit()
quit()
