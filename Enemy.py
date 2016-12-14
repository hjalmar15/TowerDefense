import pygame
from Board import *
PATH = getEnemyPath()
class Enemy(object):
    def __init__(self, path, board):
        self.path = path
        self.board = board
        self.name = 'Enemy'
        self.description = ''
        self.speed = 0.5
        self.health = 0
        self.price = 0
        self.score = 0
        self.img = ''

class yellow(Enemy):
    def __init__(self, row, col, board):
        super(yellow, self).__init__(self, path, board)
        self.name = 'Yellow'
        self.speed = 1.0
        self.health = 25
        self.description = 'Yellow is a farmer in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.price = 25
        self.score = 50
        self.img = '/Sprites/Yellow.png'

class green(Enemy):
    def __init__(self, row, col, board):
        super(green, self).__init__(self, path, board)
        self.name = 'Green'
        self.speed = 1.0
        self.health = 50
        self.description = 'Green is a civilian in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.price = 50
        self.score = 100
        self.img = '/Sprites/Green.png'

class blue(Enemy):
    def __init__(self, row, col, board):
        super(blue, self).__init__(self, path, board)
        self.name = 'Blue'
        self.speed = 2.0
        self.health = 100
        self.description = 'Green is a soldier in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.price = 100
        self.score = 200
        self.img = '/Sprites/Blue.png'

class red(Enemy):
    def __init__(self, row, col, board):
        super(red, self).__init__(self, path, board)
        self.name = 'Red'
        self.speed = 3.0
        self.health = 1000
        self.description = 'King Angry Head himself has come to destroy your kingdom!'
        self.price = 1000
        self.score = 4000
        self.img = '/Sprites/Red.png'

        
class Red(pygame.sprite.Sprite):
    count = 1
    def __init__(self):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.count = 1
       
       x,y = PATH[0]
       x *= 40
       y *= 40
       
       icon = pygame.image.load('Sprites/Red.png')
       self.image = icon
       
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
        
    def update(self):
        """ Called each frame. """
        a,b = PATH[self.count]
        #right
        if self.rect.x < (a*40) and self.rect.y >= (b*40):
            self.rect.x += 1
        #down
        elif self.rect.x >= (a*40) and self.rect.y < (b*40):
            self.rect.y += 1
        #up
        elif self.rect.x > (a*40) and self.rect.y <= (b*40):
            self.rect.x -= 1
        #left
        elif self.rect.x <= (a*40) and self.rect.y > (b*40):
            self.rect.y -= 1
        else:
            self.count += 1
            a,b = path[self.count]
