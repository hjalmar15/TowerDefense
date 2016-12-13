class Enemy(object):
    def __init__(self, path, board):
        self.path = path
        self.board = board
        self.name = 'Enemy'
        self.description = ''
        self.speed = 0.5
        self.health = 0
        self.img = ''

class yellow(Enemy):
    def __init__(self, row, col, board):
        super(yellow, self).__init__(self, path, board)
        self.name = 'Yellow'
        self.speed = 1.0
        self.health = 25
        self.description = 'Yellow is a farmer in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.img = '/Sprites/Yellow.png'

class green(Enemy):
    def __init__(self, row, col, board):
        super(green, self).__init__(self, path, board)
        self.name = 'Green'
        self.speed = 1.0
        self.health = 50
        self.description = 'Green is a civilian in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.img = '/Sprites/Green.png'

class blue(Enemy):
    def __init__(self, row, col, board):
        super(blue, self).__init__(self, path, board)
        self.name = 'Blue'
        self.speed = 2.0
        self.health = 100
        self.description = 'Green is a soldier in the angry head village that was sent by King Angry Head to destroy your kingdom'
        self.img = '/Sprites/Blue.png'

class red(Enemy):
    def __init__(self, row, col, board):
        super(red, self).__init__(self, path, board)
        self.name = 'Red'
        self.speed = 3.0
        self.health = 1000
        self.description = 'King Angry Head himself has come to destroy your kingdom!'
        self.img = '/Sprites/Red.png'

    
