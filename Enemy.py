from Board import *
PATH = getEnemyPath()
# Yellow < Green < Blue < Red

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, health, reward, type):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.type = type
       if self.type == 'Red':
           self.name = 'Red'
           self.description = 'King Angry Head himself has come to destroy your kingdom!'
           icon = pygame.image.load('Sprites/Red.png')
           self.image = icon
       elif self.type == 'Blue':
           self.name = 'Blue'
           self.description = 'Blue is a soldier in the angry head village that was sent by King Angry Head to destroy your kingdom!'
           icon = pygame.image.load('Sprites/Blue.png')
           self.image = icon
       elif self.type == 'Green':
           self.name = 'Green'
           self.description = 'Green is a civilian in the angry head village that was sent by King Angry Head to destroy your kingdom!'
           icon = pygame.image.load('Sprites/Green.png')
           self.image = icon
       elif self.type == 'Yellow':
           self.name ='Yellow'
           self.description =  'Yellow is a farmer in the angry head village that was sent by King Angry Head to destroy your kingdom'
           icon = pygame.image.load('Sprites/Yellow.png')
           self.image = icon
       self.count = 1
       self.speed = speed
       self.maxHealth = health
       self.health = health
       self.reward = reward
       x,y = PATH[0]
       x *= 40
       y *= 40

       
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
            allEnemies.remove(self)
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
                    if x.penet == 1:
                        x.kill()
                        x.remove()
                    x.penet -= 1
                elif(self.health - x.attack <= 0):
                    if x.penet == 1:
                        x.kill()
                        x.remove()
                    x.penet -= 1
                    self.kill()
                    self.remove()
                    allEnemies.remove(self)
                    gameStats[0] += self.reward
                    gameStats[3] += self.maxHealth/2
