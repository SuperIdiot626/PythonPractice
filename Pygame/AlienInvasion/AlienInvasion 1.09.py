import pygame
import sys
import os

os.chdir("D:\Code\Python\Pygame\AlienInvasion")     #强制改变路径到当先目录下

from objects    import Ship,Alien,Bullet,Bomb
from settings   import Settings
from button     import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from time       import sleep


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(self.settings.screen_scale)
        self.bullet_list=pygame.sprite.Group()                              #储存子弹
        self.alien_list=pygame.sprite.Group()                               #储存外星人
        self.create_fleet()                                                 #在初始化阶段就生成外星人
        self.ship=Ship(self)
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.play_button=Button(self,'Play')
        pygame.display.set_caption("Alien Invasion")                        #设置程序标题


    def fire_bullet(self):
        new_bullet=Bullet(self)
        self.bullet_list.add(new_bullet)

    def fire_bomb(self):
        new_bullet=Bomb(self)
        self.bullet_list.add(new_bullet)
        self.stats.bomb_number-=1
        self.sb.prep_bomb()

    def update_bullets(self):                                               #更新子弹相关内容
        for bullet in self.bullet_list.sprites():                           #遍历并显示每个子弹
            if bullet.rect.bottom<=0:                                       #删除超界的子弹
                self.bullet_list.remove(bullet)
            bullet.draw_bullet()                                            #显示子弹

        collisions=pygame.sprite.groupcollide(                              #检测子弹与外星舰队的碰撞
            self.bullet_list,self.alien_list,1,1)

        if collisions:                                                      #检测组员碰撞
            for aliens in collisions.values():                              #collisions为一字典
                self.stats.score+=self.settings.alien_score*len(aliens)     #字典键为子弹，值为与子弹碰撞的对象列表
            self.sb.prep_score()
            self.sb.check_high_score()                                      #检测是否出现了新的最高分

        if not self.alien_list:                                             #若所有舰队被消灭
            self.stats.score+=self.settings.round_score*self.stats.level    #每轮游戏额外得分为10000*等级数
            self.bullet_list.empty()                                        #清空子弹
            self.create_fleet()                                             #再次生成新的舰队
            self.settings.level_up()                                        #升级
            self.stats.level+=1
            self.stats.bomb_number+=1
            self.sb.prep_level()
            self.sb.prep_bomb()


    def create_fleet(self):
        new_alien=Alien(self)
        alien_gap_x=self.settings.alien_gapratio_x+1
        alien_gap_y=self.settings.alien_gapratio_y+1
        alien_width,alien_height=new_alien.rect.width,new_alien.rect.height #读取外星人图像参数
        for alien_y in range(self.settings.alien_numbers_y):                #遍历行
            for alien_x in range(self.settings.alien_numbers_x):            #在每一行中生成外星人
                new_alien=Alien(self)                                       #生成外星人
                new_alien.x=alien_width+alien_gap_x*alien_width*alien_x     #设定外星人坐标
                new_alien.y=alien_height+alien_gap_y*alien_height*alien_y     
                new_alien.rect.x=int(new_alien.x)                           #防止小数
                new_alien.rect.y=int(new_alien.y)
                self.alien_list.add(new_alien)                              #添加到列表中
        too_many_aliens=self.check_fleet_side_edge()
        if  too_many_aliens!=0:                                             #若添加了太多的外星人
            print('too many aliens!')
            self.alien_list.empty()                                         #清空外星舰队
            if too_many_aliens==1:
                self.settings.alien_numbers_x-=1
                self.create_fleet()
            elif too_many_aliens==2:
                self.settings.alien_numbers_y-=1
                self.create_fleet()

    def check_fleet_side_edge(self):                                        #检测舰队是否碰触左右与下边界
        for alien in self.alien_list:
            if alien.check_edge():                                          #触及侧边界，返回1
                self.settings.alien_direction*=-1
                for alien in self.alien_list:
                    alien.rect.y+=self.settings.alien_downwards
                return 1
            if alien.rect.bottom>alien.screen_rect.bottom:                  #触及底部边界，返回2
                self.ship_hit()
                return 2
        return 0                                                            #未触及任何边界则返回0

    def update_aliens(self):
        self.check_fleet_side_edge()
        for alien in self.alien_list:
            alien.draw_alien()
        if pygame.sprite.spritecollideany(self.ship,self.alien_list):
            self.ship_hit()


    def ship_hit(self):                                                     #飞船被碰撞
        if self.stats.ships_left>0:                                         #若剩余生命大于0
            self.stats.ships_left-=1                                        #减一条命
            self.alien_list.empty()                                         #清空外星舰队
            self.bullet_list.empty()                                        #清空子弹
            self.create_fleet()
            self.ship.center_ship()
            self.sb.prep_ships()
            sleep(1)
        else:
            self.stats.game_active=False
            self.stats.score=0
            pygame.mouse.set_visible(True)


    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
            if event.type==pygame.KEYDOWN:                                  #有按键按下时
                self.check_events_keydown(event)
            elif event.type==pygame.KEYUP:                                  #有按键松开时
                self.check_events_keyup(event)

    def check_events_keydown(self,event):
        if event.key == pygame.K_LSHIFT:                                    #按下左SHIFT开启加力
            self.ship.afterburner=self.settings.ship_afterburner

        if event.key == pygame.K_LEFT:                                      #更为流畅的移动设计，实现了类似天使左右键切换的功能
            self.ship.moving_left=True
            self.ship.move_horizontal=-1
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
            self.ship.move_horizontal=+1

        if event.key == pygame.K_UP:
            self.ship.moving_up=True
            self.ship.move_vertical=-1
        if event.key == pygame.K_DOWN:
            self.ship.moving_down=True
            self.ship.move_vertical=+1

        if event.key == pygame.K_SPACE:                                     #在子弹数量小于一定某一限制时再发射
            if len(self.bullet_list)<self.settings.bullet_allowed: 
                self.fire_bullet()
        if event.key == pygame.K_z:                                         #发射炸弹
            if self.stats.bomb_number!=0:
                self.fire_bomb()
                
        if event.key == pygame.K_ESCAPE:                                    #按下ESC键退出
            pygame.quit()
            sys.exit()

    def check_events_keyup(self,event):
        if event.key == pygame.K_LSHIFT:                                    #松开shift停止加力
            self.ship.afterburner=1

        if event.key == pygame.K_LEFT:                                      #更为流畅的移动设计，实现了类似天使左右键切换的功能
            self.ship.moving_left=False
            if self.ship.moving_right==True:
                self.ship.move_horizontal=+1
            else:
                self.ship.move_horizontal=0
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
            if self.ship.moving_left==True:
                self.ship.move_horizontal=-1
            else:
                self.ship.move_horizontal=0
        if event.key == pygame.K_UP:    
            self.ship.moving_up=False
            if self.ship.moving_down==True:
                self.ship.move_vertical=+1
            else:
                self.ship.move_vertical=0
        if event.key == pygame.K_DOWN:
            self.ship.moving_down=False
            if self.ship.moving_up==True:
                self.ship.move_vertical=-1
            else:
                self.ship.move_vertical=0


    def check_play_button(self,mouse_pos):
        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            pygame.mouse.set_visible(False)
            self.stats.game_active=True
            self.stats.reset_stats()
            self.sb.prep_score()                                            #修复在游戏开始后到击中第一个外星人为止显示上局分数的问题
            self.sb.prep_level()
            self.sb.prep_ships()
            self.sb.prep_bomb()
            self.settings.level_zero()
            self.alien_list.empty()                                         #清空外星舰队
            self.bullet_list.empty()                                        #清空子弹
            self.create_fleet()
            self.ship.center_ship()


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)                            #显示屏幕
        if self.stats.game_active==True:
            self.ship.draw_ship()                                           #显示飞船
            self.update_bullets()                                           #更新子弹
            self.update_aliens()
            self.sb.show_score()

        else:
            self.play_button.draw_button()
        pygame.display.flip()                                               #类似于update，永远放在所有元素绘制完毕之后

    def run_game(self):
        
        while True:
            self.check_events()
            self.update_screen()
            pygame.time.Clock().tick(60)




if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()   



#2020年12月16日20:51:16  完成了顺畅移动，可以实现类似天使左右键的功能，下一步打算添加速度量，将飞船的速度限制在某一范围内
#bug01  先按住左，再按右会使移动速度变快，并且在这种状态下会穿过边界，原因未知。其他方向也有相同的问题。原因在于进行移动判定时进行了两次速度叠加

#que01  如何实现加力？                   done   在移动速度处进行了修改，达到需要的结果
#que02  blit函数调用rect对象的作用？    

#improve01  实现加力系数的改变