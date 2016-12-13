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
        text = ['Play Game', 'Quit']
        run = True
        while run:
                screen.fill(white)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                print(event)
                font = pygame.font.Font('freesansbold.ttf',30)
                x = display_width/2
                y = display_height/2
                isClick = []
                for t in text:
                        tex = font.render(t, True, black)
                        texR = tex.get_rect()
                        texR.center = (x,y)
                        if texR.collidepoint(pygame.mouse.get_pos()):
                                tex = font.render(t, True, red)
                        screen.blit(tex, texR)
                        y += 35
                        isClick.append(texR)
                        
                if pygame.event.get(pygame.MOUSEBUTTONUP):
                        if isClick[0].collidepoint(pygame.mouse.get_pos()):
                                theGame()
                        if isClick[1].collidepoint(pygame.mouse.get_pos()):
                                pygame.quit()
                                quit()
                                
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
