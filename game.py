import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))

def introMenu():
    run = True
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        theFont = pygame.font.Font('freesansbold.ttf',30)
        newGame = theFont.render("Play Game", True, black)
        newGameR = newGame.get_rect()
        newGameR.center = ((display_width/2),(display_height/2))
        screen.blit(newGame, newGameR)

        if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if newGameR.collidepoint(pygame.mouse.get_pos()):
                        theGame()
                        
        pygame.display.update()
        clock.tick(15)
        
def theGame():
        run = True
        screen.fill(black)
        while run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                pygame.display.flip()
                
introMenu()
pygame.quit()
quit()
