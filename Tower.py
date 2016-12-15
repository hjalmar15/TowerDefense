import pygame
from Board import *
from game import *

class Tower(object):
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.name = 'Tower'
        self.attack = 0
        self.speed = 1.0
        self.rang = 0
        self.cost = 0
        self.pene = 0
        self.img = ''



class Shooter(pygame.sprite.Sprite):

    def __init__(self, row, col):
        #super(shooter, self).__init__(self, row, col, board)
        pygame.sprite.Sprite.__init__(self)

        self.name = 'Shooter'
        self.attack = 10
        self.speed = 1.0
        self.rang = 10
        self.cost = 100
        self.pene = 1

        #icon = pygame.image.load('Sprites/Shooter.png')
        icon = pic
        self.image = icon

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row


        def update(self):
            if(checkCollision(self, allSprites)):
                print('In range')


        def shoot(self, enemies):
            pass







class Bomber(pygame.sprite.Sprite):
    def __init__(self, row, col):
        #super(bomber, self).__init__(self, row, col, board)
        pygame.sprite.Sprite.__init__(self)

        self.name = 'Bomber'
        self.attack = 25
        self.speed = 2.0
        self.rang = 15
        self.cost = 150
        self.pene = 2

        icon = pygame.image.load('Sprites/BomberRange.png')
        self.image = icon

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row


        def update(self):
            pass


        def shoot(self, enemies):
            pass


class Sniper(pygame.sprite.Sprite):
    def __init__(self, row, col):
        #super(sniper, self).__init__(self, row, col, board)
        pygame.sprite.Sprite.__init__(self)

        self.name = 'Sniper'
        self.attack = 20
        self.speed = 3.0
        self.rang = 50
        self.cost = 400
        self.pene = 4

        #icon = pygame.image.load('Sprites/Sniper.png')
        icon = pic
        self.image = icon

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row


def checkCollision(obj1, obj2):
    col = pygame.sprite.collide_rect(obj1, obj2)
    return col

