import pygame.font
from pygame.sprite import Group
from objects import Ship


class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()                  #读取屏幕矩形参数
        self.settings=ai_game.settings
        self.stats=ai_game.stats

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_bomb()

    def prep_score(self):
        score_str="{:,}".format(self.stats.score)                   #在数据中插入逗号以分隔，只能用,分隔
        self.score_image=self.font.render(score_str,
            True,self.text_color,self.settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20             #右上角20像素间隔
        self.score_rect.top=20
    
    def prep_high_score(self):
        high_score=round(self.stats.high_score,-1)                  #round函数将保留n位有效数字，第二个参数指小数位数，-1就是整十
        high_score="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score,
            True,self.text_color,self.settings.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        #self.high_score_rect.right=self.screen_rect.right-20       #右上角20像素间隔
        self.high_score_rect.midtop=self.screen_rect.midtop

    def prep_level(self):
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,
            True,self.text_color,self.settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-20             #右上角20像素间隔
        self.level_rect.top=50

    def prep_bomb(self):
        bomb_number_str=str(self.stats.bomb_number)
        self.bomb_image=self.font.render(bomb_number_str,
            True,self.text_color,self.settings.bg_color)
        self.bomb_rect=self.bomb_image.get_rect()
        self.bomb_rect.right=self.screen_rect.left+220              #右上角20像素间隔
        self.bomb_rect.top=10

    def prep_ships(self):                                           #绘制剩下的飞船数量
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.score>self.stats.high_score:
            self.stats.high_score=self.stats.score
            self.prep_high_score()


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.bomb_image,self.bomb_rect)
        self.ships.draw(self.screen)