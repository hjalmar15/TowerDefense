import pygame
from Board import *
from Enemy import *

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
        self.rang = 160
        self.cost = 100
        self.pene = 1

        s = pygame.Surface((self.rang,self.rang))
        s.set_alpha(10)
        s.fill((255,255,255))
        self.image = s

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
        self.rect.x -= 60
        self.rect.y -= 60


    def update(self):
        for s in allEnemies:
            if(checkCollision(self, s)):
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
        self.rang = 160
        self.cost = 150
        self.pene = 2

        s = pygame.Surface((self.rang,self.rang))
        s.set_alpha(10)
        s.fill((255,255,255))
        self.image = s

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
        self.rect.x -= 60
        self.rect.y -= 60



    def update(self):
        for s in allEnemies:
            if(checkCollision(self, s)):
                print('In range')


    def shoot(self, enemies):
        pass


class Sniper(pygame.sprite.Sprite):
    def __init__(self, row, col):
        #super(sniper, self).__init__(self, row, col, board)
        pygame.sprite.Sprite.__init__(self)

        self.name = 'Sniper'
        self.attack = 20
        self.speed = 3.0
        self.rang = 160
        self.cost = 400
        self.pene = 4

        s = pygame.Surface((self.rang,self.rang))
        s.set_alpha(10)
        s.fill((255,255,255))
        self.image = s

        row *= 40
        col *= 40

        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
        self.rect.x -= 60
        self.rect.y -= 60

    def update(self):
        for s in allEnemies:
            if(checkCollision(self, s)):
                print('In range')


    def shoot(self, enemies):
        pass



def checkCollision(obj1, obj2):
    return pygame.sprite.collide_rect(obj1, obj2)

