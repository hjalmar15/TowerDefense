import pygame
from Board import *
import math

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
        self.bSpeed = 10
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
        self.rect.x -= self.rang / 2 - 20
        self.rect.y -= self.rang / 2 - 20


    def update(self):
        for s in allEnemies:
            if(checkCollision(self, s)):
                #startX, startY, targetX, targetY, attack, range, speed, penet
                allBullets.add(Bullet(self.rect.x + self.rang / 2 - 20, self.rect.y + self.rang / 2 - 20, s.rect.x, s.rect.y, self.attack, self.rang, self.bSpeed, self.pene))

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
        self.rect.x -= self.rang / 2 - 20
        self.rect.y -= self.rang / 2 - 20



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
        self.rect.x -= self.rang / 2 - 20
        self.rect.y -= self.rang / 2 - 20

    def update(self):
        for s in allEnemies:
            if(checkCollision(self, s)):
                print('In range')


    def shoot(self, enemies):
        pass

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX, startY, targetX, targetY, attack, range, speed, penet):
        #super(sniper, self).__init__(self, row, col, board)
        pygame.sprite.Sprite.__init__(self)

        self.name = 'Bullet'
        self.attack = attack
        self.range = range
        self.speed = speed
        self.penet = penet
        self.targetX = targetX
        self.targetY = targetY
        self.startX = startX
        self.startY = startY

        icon = pygame.image.load('Sprites/Bullet.png')
        self.image = icon

        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY
        self.bullet_vector = Move(targetX, targetY, startX, startY, speed)
    def update(self):
        self.rect.x += self.bullet_vector[0]
        self.rect.y += self.bullet_vector[1]

        if self.rect.x < 0:
            self.kill()
        if self.rect.x > 1000:
            self.kill()
        if self.rect.y < 0:
            self.kill()
        if self.rect.y > 720:
            self.kill()


def checkCollision(obj1, obj2):
    return pygame.sprite.collide_rect(obj1, obj2)


def Move(t0,t1,psx,psy,speed):
    global mx
    global my

    speed = speed

    distance = [t0 - psx, t1 - psy]
    norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / norm, distance[1 ] / norm]

    bullet_vector = [direction[0] * speed, direction[1] * speed]
    return bullet_vector