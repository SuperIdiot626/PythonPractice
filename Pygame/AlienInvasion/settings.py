class Settings:
    def __init__(self):
        self.screen_width=1200                                      #屏幕宽度
        self.screen_height=800                                      #屏幕高度
        self.bg_color=(230,230,230)                                 #背景颜色

        self.shipspeed=4                                            #飞船速度
        self.ship_limit=3                                           #飞船数量限制
        self.ship_afterburner=5                                     #设置加力的速度增量

        self.bullet_speed=5                                         #设置子弹速度
        self.bullet_width=5                                         #设置子弹宽度    
        self.bullet_height=15                                       #设置子弹高度
        self.bullet_color=(255,0,0)                                 #设置子弹颜色
        self.bullet_allowed=5                                       #设置子弹数量限制

        self.bomb_speed=5                                           #设置炸弹速度
        self.bomb_width=600                                         #设置炸弹宽度    
        self.bomb_height=10                                         #设置炸弹高度
        self.bomb_initial=3                                         #初始炸弹数量

        self.alien_direction=1                                      #外星舰队初始方向，1右，-1左
        self.alien_downwards=5                                      #每次触及侧边界，向下移动的距离
        self.alien_speed=1                                          #外星舰队速度
        self.alien_score=50                                         #外形人初始分数
        self.alien_numbers_x=8
        self.alien_numbers_y=3
        self.alien_gapratio_x=0.5
        self.alien_gapratio_y=0.5

        self.round_score=10000                                      #设定每回合完成后的份数

        self.screen_scale=(self.screen_width,self.screen_height)    #设置窗口大小
        self.alien_initial_speed=self.alien_speed
        self.alien_initial_score=self.alien_score
        self.bullet_scale=(self.bullet_width,self.bullet_height)    #设置子弹大小
        self.bomb_scale=(self.bomb_width,self.bomb_height)          #设置炸弹大小
        

    def level_up(self):
        self.alien_speed+=0.5                                       #每次升级，速度+0.5像素/帧
        self.alien_score+=10                                        #每次升级，分数+10

    def level_zero(self):                                           #等级归零
        self.alien_speed=self.alien_initial_speed
        self.alien_score=self.alien_initial_score