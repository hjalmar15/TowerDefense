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

start = Red(0, 0, 0)

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
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            if event.type == pygame.KEYDOWN:
                keyPressed = True
                pressed = pygame.key.get_pressed()
        if gameStats[1] == 10 and len(allEnemies) == 0:
            youWin()
            gameStats[1] += 1
            gameStats[0] += 100
            startWave(gameStats[1])

        if len(message) > 0:
            if messageTime > 0:
                Disp = fontMin.render(message, 1, black)
                Rect = Disp.get_rect()
                Rect.topleft = (1075, 500)
                DISPLAYSURF.blit(Disp, Rect)
                messageTime -= 1

        if mouseClicked or keyPressed:
            whatClicked = click(mousex, mousey)
            if whatClicked == 'placeSh' or pressed[pygame.K_s]:
                shooter = Shooter(1050, 200)
                if gameStats[0] >= shooter.cost:
                        placeTower(7, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80

            if whatClicked == 'placeB' or pressed[pygame.K_a]:
                bomber = Bomber(1050, 120)
                if gameStats[0] >= bomber.cost:
                        placeTower(8, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80
            if whatClicked == 'placeSn' or pressed[pygame.K_d]:
                sniper = Sniper(1050, 280)
                if gameStats[0] >= sniper.cost:
                        placeTower(9, gameStats)
                else:
                        message = "Not enough money"
                        messageTime = 80
            if (whatClicked == "start" or pressed[pygame.K_SPACE]):
                gameStats[1] += 1
                gameStats[0] += 100
                if gameStats[1] != 10:
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
    shooter = Shooter(1050, 200)
    bomber = Bomber(1050, 110)
    sniper = Sniper(1050, 280)

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
        showNewEnemy(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
    elif level == 2:
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
    elif level == 3:
        showNewEnemy(Green(3, 100, 100))
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
        queue.append(Green(3, 100, 100))
        queue.append(Green(3, 100, 100))
    elif level == 4:
        queue.append(Yellow(2, 50, 10))
        queue.append(Yellow(2, 50, 10))
        queue.append(Green(3, 100, 20))
        queue.append(Green(3, 100, 20))
        queue.append(Green(3, 100, 20))
        queue.append(Green(3, 100, 20))
    elif level == 5:
        showNewEnemy(Blue(4, 200, 100))
        for i in range(0, 5):
            queue.append(Green(3, 100, 20))
        queue.append(Blue(4, 200, 100))
    elif level == 6:
        for i in range(0, 5):
            queue.append(Green(3, 100, 20))
        for i in range(0, 5):
            queue.append(Blue(4, 200, 100))
    elif level == 7:
        for i in range(0, 5):
            queue.append(Yellow(2, 50, 10))
        for i in range(0, 5):
            queue.append(Green(3, 100, 20))
        for i in range(0, 5):
            queue.append(Blue(4, 200, 100))
    elif level == 8:
        for i in range(0, 7):
            queue.append(Yellow(2, 50, 10))
        for i in range(0, 7):
            queue.append(Green(3, 100, 20))
        for i in range(0, 7):
            queue.append(Blue(4, 200, 100))
    elif level == 9:
        for i in range(0, 10):
            queue.append(Yellow(2, 50, 10))
        for i in range(0, 10):
            queue.append(Green(3, 100, 20))
        for i in range(0, 10):
            queue.append(Blue(4, 200, 100))
    elif level == 10:
        showNewEnemy(Red(1, 1000, 500))
        for i in range(0, 10):
            queue.append(Yellow(2, 50, 10))
        for i in range(0, 10):
            queue.append(Green(3, 100, 20))
        for i in range(0, 10):
            queue.append(Blue(4, 200, 100))
        queue.append(Red(1, 5000, 500))
    else:
        red = level - 10

        if level < 15:
            multH = 2
            multS = 1.005
        if level < 20:
            multH = 3
            multS = 1.01
        if level < 25:
            multH = 4
            multS = 1.02

        for i in range(level):
            queue.append(Yellow(2*multS, 50*multH, 10))
        for i in range(level):
            queue.append(Green(3*multS, 100*multH, 20))
        for i in range(level):
            queue.append(Blue(4*multS, 200*multH, 100))
        for i in range(red):
            queue.append(Red(1*multS, 5000*multH, 100))


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
        theTower = Shooter(1050, 200)
    if tower == 8:
        mousex, mousey = 1050, 120
        theTower = Bomber(1050, 120)
    if tower == 9:
        mousex, mousey = 1050, 280
        theTower = Sniper(1050, 280)
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
        towers.draw(screen)
        allBullets.update()
        allBullets.draw(screen)

        if mouseClick == True:
            x, y = getGridAtPixel(int(mousex), int(mousey))
            x1 = int(x)
            y1 = int(y)
            if tilemap[y1][x1] == 1:

                if (tower == 7):
                    shooter = Shooter(y1, x1)
                    gameStats[0] -= shooter.cost

                    towers.add(shooter)
                if (tower == 8):
                    bomber = Bomber(y1, x1)
                    gameStats[0] -= bomber.cost

                    towers.add(bomber)
                if (tower == 9):
                    sniper = Sniper(y1, x1)
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
