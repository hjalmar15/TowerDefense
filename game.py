from Tower import *
from Enemy import *
from Board import *

pygame.init()
pygame.font.init()

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tower Defense: Angry Heads')

towers = pygame.sprite.Group()

font = pygame.font.Font('Fonts/freesansbold.ttf', 30)
fontMon = pygame.font.Font('Fonts/freesansbold.ttf', 22)
fontMin = pygame.font.Font('Fonts/freesansbold.ttf', 15)
fontStats = pygame.font.Font('Fonts/freesansbold.ttf', 12)

start = Enemy(0, 0, 0, 'Red')

prev = []
queue = []


def introMenu():
    # list of menu text
    text = ['Play Game', 'Quit']
    run = True
    bg = pygame.image.load("Sprites/BoostedHeads.png")

    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1)
    while run:
        mouseClicked = False
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = True

        x = display_width / 2
        y = display_height / 3
        # isClick = stores location of menu items "rect"
        isClick = []

        # writes menu text, diff col if mouseover
        for t in text:
            tex = font.render(t, True, black)
            texR = tex.get_rect()
            texR.center = (x, y)
            if texR.collidepoint(pygame.mouse.get_pos()):
                tex = font.render(t, True, red)
            screen.blit(tex, texR)
            y += 50
            isClick.append(texR)
        # clickable menu items
        if mouseClicked and isClick[0].collidepoint(event.pos):
            theGame()
        if mouseClicked and isClick[1].collidepoint(event.pos):
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)


def theGame():
    # Initialize mouse and screen
    pygame.mixer.music.stop()
    screen.fill(black)
    mousex = 0
    mousey = 0
    selectedTower = None
    # Initialize game
    run = True
    message = ()
    messageTime = 0
    pos = 0
    while run:
        drawBoard()
        drawButtons()
        drawQueue()
        drawStats(gameStats)
        mouseClicked = False
        keyPressed = False
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            if event.type == pygame.KEYDOWN:
                keyPressed = True
                pressed = pygame.key.get_pressed()

        if messageTime == 0:
            message = "Mouse over enemy for HP"
            messageTime = 5

        if gameStats[1] == 10 and len(allEnemies) == 0:
            youWin()
            gameStats[1] += 1
            gameStats[0] += 100
            startWave(gameStats[1])

        if len(message) > 0:
            if messageTime > 0:
                Disp = fontMin.render(message, 1, black)
                Rect = Disp.get_rect()
                Rect.topleft = (1050, 500)
                DISPLAYSURF.blit(Disp, Rect)
                messageTime -= 1


        for x in allEnemies:
            if x.rect.collidepoint(pos):
                message = "Health: "+ str(x.health) +"/"+ str(x.maxHealth)
                messageTime = 120

        if mouseClicked or keyPressed:
            whatClicked = click(mousex, mousey)
            if whatClicked == 'placeSh' or pressed[pygame.K_s]:
                shooter = Tower(1050, 200, 'Shooter')
                if gameStats[0] >= shooter.cost:
                        placeTower(7, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80

            if whatClicked == 'placeB' or pressed[pygame.K_a]:
                bomber = Tower(1050, 120, 'Bomber')
                if gameStats[0] >= bomber.cost:
                        placeTower(8, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80
            if whatClicked == 'placeSn' or pressed[pygame.K_d]:
                sniper = Tower(1050, 280, 'Sniper')
                if gameStats[0] >= sniper.cost:
                        placeTower(9, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80
            if (whatClicked == "start" or pressed[pygame.K_SPACE]) and (gameStats[1] < 10 or gameStats[1] > 10):
                gameStats[1] += 1
                gameStats[0] += 100
                startWave(gameStats[1])

        if gameStats[2] == 0:
            gameOver()

        allEnemies.update()
        allEnemies.draw(screen)
        allBullets.update()
        allBullets.draw(screen)
        towers.update()
        pygame.display.flip()
        clock.tick(60)


def drawStats(gameStats):
    # Players stats
    moneyDisp = fontMon.render('Money: %d' % gameStats[0], 1, black)
    moneyRect = moneyDisp.get_rect()
    moneyRect.topleft = (1080, 610)
    DISPLAYSURF.blit(moneyDisp, moneyRect)

    levelDisp = font.render('Level: %d' % gameStats[1], 1, white)
    levelRect = moneyDisp.get_rect()
    levelRect.topleft = (10, 0)
    DISPLAYSURF.blit(levelDisp, levelRect)

    livesDisp = font.render('Lives: %d' % gameStats[2], 1, white)
    livesRect = moneyDisp.get_rect()
    livesRect.topleft = (875, 0)
    DISPLAYSURF.blit(livesDisp, livesRect)

    scoreDisp = font.render('Score: %d' % gameStats[3], 1, white)
    scoreRect = scoreDisp.get_rect()
    scoreRect.topleft = (450, 0)
    DISPLAYSURF.blit(scoreDisp, scoreRect)

    # Tower stats
    shooter = Tower(1050, 200,'Shooter')
    bomber = Tower(1050, 110,'Bomber')
    sniper = Tower(1050, 280,'Sniper')

    # Bomber
    bomberDisp = fontMin.render('Bomber', 1, black)
    bomberRect = bomberDisp.get_rect()
    bomberRect.topleft = (1100, 110)
    DISPLAYSURF.blit(bomberDisp, bomberRect)

    bomberStatsDisp = fontStats.render('Damage: %d' % bomber.attack + '  Speed: %d' % (bomber.speed*2), 1, black)
    bomberStatsRect = bomberStatsDisp.get_rect()
    bomberStatsRect.topleft = (1100, 130)
    DISPLAYSURF.blit(bomberStatsDisp, bomberStatsRect)

    bomberRangDisp = fontStats.render('Range: %d' % bomber.rang + '  Cost: %d' % bomber.cost, 1, black)
    bomberRangRect = bomberRangDisp.get_rect()
    bomberRangRect.topleft = (1100, 145)
    DISPLAYSURF.blit(bomberRangDisp, bomberRangRect)

    # Shooter
    shooterDisp = fontMin.render('Shooter', 1, black)
    shooterRect = shooterDisp.get_rect()
    shooterRect.topleft = (1100, 200)
    DISPLAYSURF.blit(shooterDisp, shooterRect)

    shooterStatsDisp = fontStats.render('Damage: %d' % shooter.attack + '  Speed: %d' % (shooter.speed*2), 1, black)
    shooterStatsRect = shooterStatsDisp.get_rect()
    shooterStatsRect.topleft = (1100, 220)
    DISPLAYSURF.blit(shooterStatsDisp, shooterStatsRect)

    shooterRangDisp = fontStats.render('Range: %d' % shooter.rang + '  Cost: %d' % shooter.cost, 1, black)
    shooterRangRect = shooterRangDisp.get_rect()
    shooterRangRect.topleft = (1100, 235)
    DISPLAYSURF.blit(shooterRangDisp, shooterRangRect)

    # Sniper
    sniperDisp = fontMin.render('Sniper', 1, black)
    sniperRect = sniperDisp.get_rect()
    sniperRect.topleft = (1100, 280)
    DISPLAYSURF.blit(sniperDisp, sniperRect)

    sniperStatsDisp = fontStats.render('Damage: %d' % sniper.attack + '  Speed: %d' % (sniper.speed*2), 1, black)
    sniperStatsRect = sniperStatsDisp.get_rect()
    sniperStatsRect.topleft = (1100, 300)
    DISPLAYSURF.blit(sniperStatsDisp, sniperStatsRect)

    sniperRangDisp = fontStats.render('Range: %d' % sniper.rang + '  Cost: %d' % sniper.cost, 1, black)
    sniperRangRect = sniperRangDisp.get_rect()
    sniperRangRect.topleft = (1100, 315)
    DISPLAYSURF.blit(sniperRangDisp, sniperRangRect)

    # Information stats


def drawQueue():
    if len(queue) > 0:
        if len(prev) == 0:
            creep = queue.pop()
            prev.append(creep)
            allEnemies.add(creep)
        elif not pygame.sprite.collide_rect(start, prev[0]):
            creep = queue.pop()
            prev[0] = (creep)
            allEnemies.add(creep)
        elif prev[0] not in allEnemies:
            creep = queue.pop()
            prev[0] = (creep)
            allEnemies.add(creep)


def click(mousex, mousey):
    if mousex >= 1050 and mousex <= 1090 and mousey >= 120 and mousey <= 160:
        return 'placeB'
    elif mousex >= 1050 and mousex <= 1090 and mousey >= 200 and mousey <= 240:
        return 'placeSh'
    elif mousex >= 1050 and mousex <= 1090 and mousey >= 280 and mousey <= 320:
        return 'placeSn'
    elif mousex >= 1050 and mousex <= 1230 and mousey >= 650 and mousey <= 710:
        return 'start'
    else:
        return None


def startWave(level):
    # Yellow < Green < Blue < Red

    if level == 1:
        showNewEnemy(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
    elif level == 2:
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
    elif level == 3:
        showNewEnemy(Enemy(4, 250, 100,'Green'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(4, 250, 100,'Green'))
        queue.append(Enemy(4, 250, 100,'Green'))
    elif level == 4:
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(3, 100, 10,'Yellow'))
        queue.append(Enemy(4, 250, 20,'Green'))
        queue.append(Enemy(4, 250, 20,'Green'))
        queue.append(Enemy(4, 250, 20,'Green'))
        queue.append(Enemy(4, 250, 20,'Green'))
    elif level == 5:
        showNewEnemy(Enemy(5, 500, 100,'Blue'))
        for i in range(0, 5):
            queue.append(Enemy(4, 250, 20,'Green'))
        queue.append(Enemy(5, 500, 100,'Blue'))
    elif level == 6:
        for i in range(0, 5):
            queue.append(Enemy(4, 250, 20,'Green'))
        for i in range(0, 5):
            queue.append(Enemy(5, 500, 100,'Blue'))
    elif level == 7:
        for i in range(0, 5):
            queue.append(Enemy(3, 100, 10,'Yellow'))
        for i in range(0, 5):
            queue.append(Enemy(4, 250, 20,'Green'))
        for i in range(0, 5):
            queue.append(Enemy(5, 500, 100,'Blue'))
    elif level == 8:
        for i in range(0, 7):
            queue.append(Enemy(3, 100, 10,'Yellow'))
        for i in range(0, 7):
            queue.append(Enemy(4, 250,20,'Green'))
        for i in range(0, 7):
            queue.append(Enemy(5, 500, 100,'Blue'))
    elif level == 9:
        for i in range(0, 10):
            queue.append(Enemy(3, 100, 10,'Yellow'))
        for i in range(0, 10):
            queue.append(Enemy(4, 250, 20,'Green'))
        for i in range(0, 10):
            queue.append(Enemy(5, 500, 100,'Blue'))
    elif level == 10:
        showNewEnemy(Enemy(2, 10000, 500,'Red'))
        for i in range(0, 10):
            queue.append(Enemy(3, 100, 10,'Yellow'))
        for i in range(0, 10):
            queue.append(Enemy(4, 250, 20,'Green'))
        for i in range(0, 10):
            queue.append(Enemy(5, 500, 100,'Blue'))
        queue.append(Enemy(2, 10000, 500,'Red'))
    else:
        red = level - 10

        if level > 10 and level < 15:
            multH = 1.5
            multS = 1.01
        if level >= 15 and level < 20:
            multH = 2
            multS = 1.1
        if level >= 20:
            multH = 4
            multS = 1.5

        for i in range(level):
            queue.append(Enemy(3*multS, 100*multH, 10, 'Yellow'))
        for i in range(level):
            queue.append(Enemy(4*multS, 250*multH, 20, 'Green'))
        for i in range(level):
            queue.append(Enemy(5*multS, 500*multH, 100, 'Blue'))
        for i in range(red):
            queue.append(Enemy(2*multS, 10000*multH, 100, 'Red'))


def showNewEnemy(EnemyObj):
    runNewEnemy = True
    screen.blit(textures[16], (220, 250))
    enemyObjDesc = fontStats.render('%s' % EnemyObj.description, 1, white)
    enemyObjRect = enemyObjDesc.get_rect()
    enemyObjRect.topleft = (230, 300)
    screen.blit(enemyObjDesc, enemyObjRect)
    if EnemyObj.name == 'Yellow':
        screen.blit(textures[17], (320, 340))
    elif EnemyObj.name == 'Green':
        screen.blit(textures[18], (320, 340))
    elif EnemyObj.name == 'Blue':
        screen.blit(textures[19], (320, 340))
    else:
        screen.blit(textures[20], (320, 340))
    enemyStat = fontStats.render('Health: %d' % EnemyObj.maxHealth + '   Speed: %d' % EnemyObj.speed + '   Reward: %d' % EnemyObj.reward, 1, white)
    enemyRect = enemyStat.get_rect()
    enemyRect.topleft = (400, 350)
    screen.blit(enemyStat, enemyRect)

    pygame.display.flip()
    while runNewEnemy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                runNewEnemy = False


def placeTower(tower, gameStats):
    runIt = True
    theTower = None
    if tower == 7:
        mousex, mousey = 1050, 200
        theTower = Tower(1050, 200,'Shooter')
    if tower == 8:
        mousex, mousey = 1050, 120
        theTower = Tower(1050, 120, 'Bomber')
    if tower == 9:
        mousex, mousey = 1050, 280
        theTower = Tower(1050, 280, 'Sniper')
    mousex += 20
    mousey += 20
    while runIt:
        drawBoard()
        drawButtons()
        drawStats(gameStats)
        mouseClick = False
        keyPressed = False
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClick = True
            if event.type == pygame.KEYDOWN:
                keyPressed = True
                pressed = pygame.key.get_pressed()
        img = textures[tower]
        screen.blit(img, (mousex - 20, mousey - 20))

        if keyPressed:
            if pressed[pygame.K_ESCAPE]:
                runIt = False
        s = pygame.Surface((theTower.rang, theTower.rang))
        s.set_alpha(10)
        s.fill((255,255,255))
        screen.blit(s, (mousex - theTower.rang/2, mousey - theTower.rang/2))

        allEnemies.update()
        allEnemies.draw(screen)
        towers.update()
        allBullets.update()
        allBullets.draw(screen)

        if mouseClick == True:
            x, y = getGridAtPixel(int(mousex), int(mousey))
            x1 = int(x)
            y1 = int(y)
            if tilemap[y1][x1] == 1:

                if (tower == 7):
                    shooter = Tower(y1, x1,'Shooter')
                    gameStats[0] -= shooter.cost

                    towers.add(shooter)
                if (tower == 8):
                    bomber = Tower(y1, x1, 'Bomber')
                    gameStats[0] -= bomber.cost

                    towers.add(bomber)
                if (tower == 9):
                    sniper = Tower(y1, x1, 'Sniper')
                    gameStats[0] -= sniper.cost

                    towers.add(sniper)

                tilemap[y1][x1] = tower
                runIt = False

        pygame.display.flip()
        clock.tick(60)


def getGridAtPixel(mousex, mousey):
    x = (mousex) / 40
    y = (mousey) / 40
    if x >= 0 and x <= 32 and y >= 0 and y <= 18:
        return x, y


def youWin():
    DISPLAYSURF.blit(textures[11], (350, 220))
    runWin = True
    pygame.display.flip()
    while runWin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                runWin = False



def gameOver():
    screen.blit(textures[15], (350, 220))
    runDefeat = True
    pygame.display.flip()
    while runDefeat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pygame.quit()
                quit()


introMenu()
pygame.quit()
quit()
