class GameStats:
    def __init__(self,ai_game):
        self.settings=ai_game.settings                              #读取设定
        self.score=0
        self.level=1
        self.high_score=0
        self.bomb_number=self.settings.bomb_initial
        self.ships_left=self.settings.ship_limit
        self.reset_stats()
        self.game_active=False



    def reset_stats(self):
        self.score=0
        self.level=1
        self.ships_left=self.settings.ship_limit
        self.bomb_number=self.settings.bomb_initial