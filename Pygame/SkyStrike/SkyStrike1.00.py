import pygame
from pygame.locals import *
import time 
import random 

class HeroPlane(object):
    def __init__(self,screen):
        self.x=230       #定义坐标
        self.y=600
        self.screen=screen
        self.imageName="./feiji/hero.png"    #英雄飞机图片
        self.image=pygame.image.load(self.imageName).convert()
        self.bulletList=[]           #储存飞机发射的子弹
    def display(self):         
        self.screen.blit(self.image,(self.x,self.y))   #更新飞机位置
        needDelItemList=[]
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
    def moveLeft(self):
        self.x-=10
    def moveRight(self):
        self.x+=10
    def moveUP(self):
        self.y-=10
    def moveDOWN(self):
        self.y+=10
    def sheBullet(self):
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

class EnemyPlane(object):
    def __init__(self,screen):
        self.x=0
        self.y=0
        self.screen=screen
        self.imageName="./feiji/enemy-1.png"
        self.image=pygame.image.load(self.imageName).convert()
        self.bulletList=[]
        self.direction="right"
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        needDelItemList=[]
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)        
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
    def move(self):
        if self.direction=="right":
            self.x+=2
        elif self.direction=="left":
            self.x-=2
        if self.x>480-50:
            self.direction="left"
        elif self.x<0:
            self.direction="right"
    def sheBullet(self):
        num=random.randint(1,100)
        if num==50:
            newBullet=EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
            
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x=x+40
        self.y=y-20 
        self.screen=screen
        self.image=pygame.image.load("./feiji/bullet-3.png").convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=3
    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x+30
        self.y=y+30 
        self.screen=screen
        self.image=pygame.image.load("./feiji/bullet-1.png").convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=3
    def judge(self):
        if self.y>890:
            return True
        else:
            return False

if __name__=='__main__':
    pygame.init()
    pygame.display.set_caption("Sky Strike")
    screen=pygame.display.set_mode((480,890),0,32)
    bgImageFile='./feiji/background.png'
    background=pygame.image.load(bgImageFile).convert()
    heroPlane=HeroPlane(screen)
    enemyPlane=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))              #控制背景图片刷新
        heroPlane.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.sheBullet()
        for event in pygame.event.get():
            if event.type==QUIT:
                print('exit')
                exit()
            if event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    heroPlane.moveLeft()
                elif event.key==K_d or event.key==K_RIGHT:
                    heroPlane.moveRight()
                elif event.key==K_w or event.key==K_UP:
                    heroPlane.moveUP()
                elif event.key==K_s or event.key==K_DOWN:
                    heroPlane.moveDOWN()
                elif event.key==K_SPACE:
                    heroPlane.sheBullet()    
        time.sleep(0.01)
        pygame.display.update()

#实现了最基本的功能，从零到一