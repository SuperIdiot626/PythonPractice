#from pygame     import font
import pygame
class Button:
    def __init__(self,ai_games,msg):
        self.screen=ai_games.screen
        self.screen_rect=self.screen.get_rect()

        self.width,self.height=200,50
        self.color_button=(50,255,50)
        self.color_text=(50,50,50)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)       #Rect 左上角坐标+长宽
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.color_text,self.color_button)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.color_button,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)