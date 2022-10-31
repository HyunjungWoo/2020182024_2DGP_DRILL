class Player:
    name = 'Player'

    def __init__(self):
        self.x = 0
    
    def where(self):
        print(self.x)

player = Player()
player.where()

Player.where(player)