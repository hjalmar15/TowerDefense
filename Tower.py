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

class shooter(Tower):
    def __init__(self, row, col, board):
        super(shooter, self).__init__(self, row, col, board)
        self.name = 'Shooter'
        self.attack = 10
        self.speed = 1.0
        self.rang = 10
        self.cost = 100
        self.pene = 1
        self.img = '/Sprites/Shooter.png'

class bomber(Tower):
    def __init__(self, row, col, board):
        super(bomber, self).__init__(self, row, col, board)
        self.name = 'Bomber'
        self.attack = 25
        self.speed = 2.0
        self.rang = 15
        self.cost = 150
        self.pene = 2
        self.img = '/Sprites/Bomber.png'

class sniper(Tower):
    def __init__(self, row, col, board):
        super(sniper, self).__init__(self, row, col, board)
        self.name = 'Sniper'
        self.attack = 20
        self.speed = 3.0
        self.rang = 50
        self.cost = 400
        self.pene = 4
        self.img = '/Sprites/Sniper.png'

    
