import pygame,sys
from pygame.locals import *
import time

pygame.init()
Surface=pygame.display.set_mode((480,640))
pygame.display.set_caption('Moonie')
TitleFro=pygame.font.Font('freesansbold.ttf',70)
GameTitle1=TitleFro.render('Moonie!',True,(0,0,200))
GameTitle2=TitleFro.render('Moonie!',True,(255,255,255))
Start=TitleFro.render('START!',True,(200,0,0))


n=0
while 1:
    Surface.blit(GameTitle1,(100,100))
    pygame.display.update()
    time.sleep(0.08)
    Surface.blit(GameTitle2,(100,100))
    pygame.display.update()
    time.sleep(0.08)
    n+=1
    if n>5:
        Surface.blit(Start,(110,200))
        pygame.display.update()
    if n==12:
        break
    for event in pygame.event.get(): 
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

class Ball(object):
    def __init__(self,surface):
        self.v_x=0
        self.v_y=0
        self.x=240
        self.y=320
        self.a_x=0
        self.a_y=0
        self.surface=surface
        self.image=pygame.image.load("./greenball.png").convert()

    def punch(self):
        if self.x<0 or self.x>480:
            self.v_x=-self.v_x
        if self.y<0 or self.y>640:
            self.v_y=-self.v_y

    def move(self):
        self.x+=self.v_x
        self.y+=self.v_y

    def accelerate(self):
        if self.v_x<=30:
            self.v_x+=self.a_x
        if self.v_y<=30:
            self.v_y+=self.a_y


ball=Ball(Surface)
while 1:
    Surface.fill((0,0,0))
    Surface.blit(ball.image,(ball.x,ball.y))
    ball.move()
    ball.accelerate()
    ball.punch()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 
            if event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    ball.a_x=-1
                elif event.key==K_d or event.key==K_RIGHT:
                    ball.a_x=+1
                elif event.key==K_w or event.key==K_UP:
                    ball.a_y=-1
                elif event.key==K_s or event.key==K_DOWN:
                    ball.a_y=+1  
                elif event.key==K_SPACE:
                    if ball.v_y>0:
                        ball.v_y=ball.v_y-5
                    if ball.v_y<0:
                        ball.v_y=ball.v_y+5
                    if ball.v_x>0:
                        ball.v_x=ball.v_x-5
                    if ball.v_x<0:
                        ball.v_x=ball.v_x+5
            elif event.type==KEYUP:
                ball.a_y=0
                ball.a_x=0
    pygame.display.update()
    pygame.time.Clock().tick(30)

#完成从零到一，改进方向：①球替换成圆形②添加速度显示器、时间显示器③添加敌人④添加开始菜单选择