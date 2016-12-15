import pygame
from Board import *
PATH = getEnemyPath()
# Yellow < Green < Blue < Red


class Yellow(pygame.sprite.Sprite):
    def __init__(self, speed, health, reward):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.count = 1
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.reward = reward
        self.description = 'Yellow is a farmer in the angry head village that was sent by King Angry Head to destroy your kingdom'
        x, y = PATH[0]
        x *= 40
        y *= 40

        icon = pygame.image.load('Sprites/Yellow.png')
        self.image = icon

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Called each frame. """
        if self.rect.x == (PATH[-1][0] * 40) and self.rect.y == (PATH[-1][1] * 40):
            gameStats[2] -= 1
            self.kill()
            self.remove()
        a, b = PATH[self.count]
        # right
        if self.rect.x < (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x + self.speed) > (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x += self.speed
        # down
        elif self.rect.x == (a * 40) and self.rect.y < (b * 40):
            if (self.rect.y + self.speed) > (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y += self.speed
        # left
        elif self.rect.x > (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x - self.speed) < (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x -= self.speed
        # up
        elif self.rect.x == (a * 40) and self.rect.y > (b * 40):
            if (self.rect.y - self.speed) < (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y -= self.speed
        else:
            if self.count + 1 < len(PATH):
                self.count += 1
            a, b = PATH[self.count]
        for x in allBullets:
            if pygame.sprite.collide_rect(x, self):
                if(self.health - x.attack > 0):
                    self.health -= x.attack
                    x.kill()
                    x.remove()
                elif(self.health - x.attack <= 0):
                    x.kill()
                    x.remove()
                    self.kill()
                    self.remove()
                    gameStats[0] += self.reward
                    gameStats[3] += self.maxHealth


class Green(pygame.sprite.Sprite):
    def __init__(self, speed, health, reward):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.count = 1
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.reward = reward
        self.description = 'Green is a civilian in the angry head village that was sent by King Angry Head to destroy your kingdom!'
        x, y = PATH[0]
        x *= 40
        y *= 40

        icon = pygame.image.load('Sprites/Green.png')
        self.image = icon

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Called each frame. """
        if self.rect.x == (PATH[-1][0] * 40) and self.rect.y == (PATH[-1][1] * 40):
            gameStats[2] -= 1
            self.kill()
            self.remove()
        a, b = PATH[self.count]
        # right
        if self.rect.x < (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x + self.speed) > (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x += self.speed
        # down
        elif self.rect.x == (a * 40) and self.rect.y < (b * 40):
            if (self.rect.y + self.speed) > (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y += self.speed
        # left
        elif self.rect.x > (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x - self.speed) < (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x -= self.speed
        # up
        elif self.rect.x == (a * 40) and self.rect.y > (b * 40):
            if (self.rect.y - self.speed) < (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y -= self.speed
        else:
            if self.count + 1 < len(PATH):
                self.count += 1
            a, b = PATH[self.count]
        for x in allBullets:
            if pygame.sprite.collide_rect(x, self):
                if(self.health - x.attack > 0):
                    self.health -= x.attack
                    x.kill()
                    x.remove()
                elif(self.health - x.attack <= 0):
                    x.kill()
                    x.remove()
                    self.kill()
                    self.remove()
                    gameStats[0] += self.reward
                    gameStats[3] += self.maxHealth


class Blue(pygame.sprite.Sprite):
    def __init__(self, speed, health, reward):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.count = 1
        self.speed = speed
        self.maxHealth = health
        self.health = health
        self.reward = reward
        self.description = 'Blue is a soldier in the angry head village that was sent by King Angry Head to destroy your kingdom!'
        x, y = PATH[0]
        x *= 40
        y *= 40

        icon = pygame.image.load('Sprites/Blue.png')
        self.image = icon

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """ Called each frame. """
        if self.rect.x == (PATH[-1][0] * 40) and self.rect.y == (PATH[-1][1] * 40):
            gameStats[2] -= 1
            self.kill()
            self.remove()
        a, b = PATH[self.count]
        # right
        if self.rect.x < (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x + self.speed) > (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x += self.speed
        # down
        elif self.rect.x == (a * 40) and self.rect.y < (b * 40):
            if (self.rect.y + self.speed) > (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y += self.speed
        # left
        elif self.rect.x > (a * 40) and self.rect.y == (b * 40):
            if (self.rect.x - self.speed) < (a * 40):
                self.rect.x = (a * 40)
            else:
                self.rect.x -= self.speed
        # up
        elif self.rect.x == (a * 40) and self.rect.y > (b * 40):
            if (self.rect.y - self.speed) < (b * 40):
                self.rect.y = (b * 40)
            else:
                self.rect.y -= self.speed
        else:
            if self.count + 1 < len(PATH):
                self.count += 1
            a, b = PATH[self.count]

        for x in allBullets:
            if pygame.sprite.collide_rect(x, self):
                if(self.health - x.attack > 0):
                    self.health -= x.attack
                    x.kill()
                    x.remove()
                elif(self.health - x.attack <= 0):
                    x.kill()
                    x.remove()
                    self.kill()
                    self.remove()
                    gameStats[0] += self.reward
                    gameStats[3] += self.maxHealth

class Red(pygame.sprite.Sprite):
    def __init__(self, speed, health, reward):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.count = 1
       self.speed = speed
       self.maxHealth = health
       self.health = health
       self.reward = reward
       self.description = 'King Angry Head himself has come to destroy your kingdom!'
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
        if self.rect.x == (PATH[-1][0]*40) and self.rect.y == (PATH[-1][1]*40):
            gameStats[2] -= 1
            self.kill()
            self.remove()
        a,b = PATH[self.count]
        #right
        if self.rect.x < (a*40) and self.rect.y == (b*40):
            if (self.rect.x + self.speed) > (a*40):
                self.rect.x = (a*40)
            else:
                self.rect.x += self.speed
        #down
        elif self.rect.x == (a*40) and self.rect.y < (b*40):
            if (self.rect.y + self.speed) > (b*40):
                self.rect.y = (b*40)
            else:
                self.rect.y += self.speed
        #left
        elif self.rect.x > (a*40) and self.rect.y == (b*40):
            if (self.rect.x - self.speed) < (a*40):
                self.rect.x = (a*40)
            else:
                self.rect.x -= self.speed
        #up
        elif self.rect.x == (a*40) and self.rect.y > (b*40):
            if (self.rect.y - self.speed) < (b*40):
                self.rect.y = (b*40)
            else:
                self.rect.y -= self.speed
        else:
            if self.count+1 < len(PATH):
                self.count += 1
            a,b = PATH[self.count]
        for x in allBullets:
            if pygame.sprite.collide_rect(x, self):
                if(self.health - x.attack > 0):
                    self.health -= x.attack
                    x.kill()
                    x.remove()
                elif(self.health - x.attack <= 0):
                    x.kill()
                    x.remove()
                    self.kill()
                    self.remove()
                    gameStats[0] += self.reward
                    gameStats[3] += self.maxHealth
