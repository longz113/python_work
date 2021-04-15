import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ai_set,ship):
        super().__init__()
        self.screen=screen
        #在(0,0)位置创建一个矩形矩形(子弹)并设置其初始位置
        self.rect=pygame.Rect(0,0,ai_set.bullet_width,ai_set.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        #设置子弹的颜色和移动速度
        self.bullet_speed=ai_set.bullet_speed
        self.bullet_color=ai_set.bullet_color

        


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
    
