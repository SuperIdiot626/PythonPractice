import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen                                  #将ai_game赋值给screen对象
        self.settings=ai_game.settings                              #读取游戏设置
        self.screen_rect=ai_game.screen.get_rect()                  #读取屏幕矩形参数

        self.moving_left=False                                      #用来保持移动状态
        self.moving_right=False
        self.moving_up=False
        self.moving_down=False

        self.move_horizontal=0                                      #是否进行移动
        self.move_vertical=0

        self.afterburner=1                                          #发动机加力

        self.image = pygame.image.load('images/ship.bmp')           #读取图片
        self.rect=self.image.get_rect()                             #读取自己所在的矩形位置
        self.rect.midbottom = self.screen_rect.midbottom            #把自己置于屏幕下边界中心    Rect.midbottom 为某一矩形的下边界中点坐标
        self.x=float(self.rect.x)                                   #防止小数
        self.y=float(self.rect.y)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom            #把自己置于屏幕下边界中心    Rect.midbottom 为某一矩形的下边界中点坐标
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def update(self):
        if (self.rect.left>self.screen_rect.left 
            and self.move_horizontal==-1):                          #若飞船在左边界之内
            self.x+=(self.move_horizontal*
                self.settings.shipspeed*self.afterburner)           #方向*速度*加力系数
        if (self.rect.right<self.screen_rect.right 
            and self.move_horizontal==+1):                          #若飞船在右边界之内
            self.x+=(self.move_horizontal*
                self.settings.shipspeed*self.afterburner)

        if (self.rect.top>self.screen_rect.top 
            and self.move_vertical==-1):                            #若飞船在上边界之内
            self.y+=(self.move_vertical*
                self.settings.shipspeed*self.afterburner)
        elif (self.rect.bottom<self.screen_rect.bottom 
            and self.move_vertical==+1):                            #若飞船在下边界之内
            self.y+=(self.move_vertical*
                self.settings.shipspeed*self.afterburner)
        
        self.rect.x=self.x                                          #为了实现小数移动
        self.rect.y=self.y

    def draw_ship(self): 
        self.update()      
        self.screen.blit(self.image,self.rect)                      #显示自己


class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen                                  #赋值屏幕对象
        self.settings=ai_game.settings                              #读取设定
        self.screen_rect=ai_game.screen.get_rect()                  #读取屏幕矩形参数
        self.image = pygame.image.load('images/alien.bmp')          #读取图片
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width                                 #获得靠近角落的坐标
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)                                   #为了实现小数的移动
        self.y=float(self.rect.y)                                   #为了实现小数的移动
        self.direction=1

    def check_edge(self):
        if (self.rect.left<self.screen_rect.left 
            or self.rect.right>self.screen_rect.right):             #若飞船在左边界之内
            return True

    def update(self):
        self.x+=self.settings.alien_speed*self.settings.alien_direction
        self.rect.x=self.x
            
    def draw_alien(self):
        self.update()
        self.screen.blit(self.image,self.rect)


class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()                                          #继承Sprite的各项属性???
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color                       #设置颜色
        self.rect=pygame.Rect(ai_game.ship.rect.midtop,self.settings.bullet_scale)
        self.rect.midtop=ai_game.ship.rect.midtop
        self.y=float(self.rect.y)
    
    def update(self):
        self.y-=self.settings.bullet_speed                          #进行移动
        self.rect.y=self.y                                          #作用？？

    def draw_bullet(self):
        self.update()
        pygame.draw.rect(self.screen,self.color,self.rect)

class Bomb(Sprite):
    def __init__(self,ai_game):
        super().__init__()                                          #继承Sprite的各项属性???
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color                       #设置颜色
        self.rect=pygame.Rect(ai_game.ship.rect.midtop,self.settings.bomb_scale)
        self.rect.midtop=ai_game.ship.rect.midtop
        self.y=float(self.rect.y)
    
    def update(self):
        self.y-=self.settings.bullet_speed                          #进行移动
        self.rect.y=self.y                                          #作用？？

    def draw_bullet(self):
        self.update()
        pygame.draw.rect(self.screen,self.color,self.rect)

class BulletPicture(Sprite):
    def __init__(self,ai_game):
        super().__init__()                                          #继承Sprite的各项属性???
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        #self.image=pygame.image.load('images/bullet.png')          #读取图片
        self.image=pygame.image.load('images/lazer.png')            #读取图片
        self.rect=self.image.get_rect()  
        self.rect.midtop=ai_game.ship.rect.midtop
        self.y=float(self.rect.y)
    
    def update(self):
        self.y-=self.settings.bullet_speed                          #进行移动
        self.rect.y=self.y                                          #作用？？

    def draw_bullet(self):
        self.update()
        self.screen.blit(self.image,self.rect)