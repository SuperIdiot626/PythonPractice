import pygame
from pygame.locals import *
from sys import exit

pygame.init()             #初始化pygame   有何用？
pygame.display.set_caption("图片移动测试")        #设置程序标题
screen=pygame.display.set_mode((1000,1000),0,32)   #设置程序大小
a=pygame.image.load('luo.png').convert()        #设置图片
 
x,y=0,0
move_x,move_y=0,0
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT or event.key==K_a:
                move_x=-1
            elif event.key==K_RIGHT or event.key==K_d:
                move_x=+1
            elif event.key==K_UP or event.key==K_w:
                move_y=-1
            elif event.key==K_DOWN or event.key==K_s:
                move_y=1
        elif event.type==KEYUP:
            move_x=0
            move_y=0
    x+=move_x
    y+=move_y
    screen.fill((124,0,0,128))     #以RGB参数设置背景图像
    screen.blit(a,(x,y))       #将图片a放置在坐标x，y处
    pygame.display.update()    #？？？？

    mycolor=pygame.Color(0,255,0,128)