class Settings():
    def __init__(self):
        #窗口设置
        self.screen_width=1200
        self.screen_height=800
        self.screen_bg_color=(200,230,230)
        #飞船的参数
        self.ship_speed=0.5
        self.ship_limit=2
        #子弹的参数
        self.bullet_width=10
        self.bullet_height=8
        self.bullet_color=(0,0,0)
        self.bullet_speed=1
        self.bullet_number=20
        #外星人的参数
        self.alien_speed_drop=0.1   #下降的速度
        self.alien_speed_dropincresae=0.5   #下降的速度
        self.alien_speed_factor=0.3   #左右移动的速度
