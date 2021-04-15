import pygame
class Ship():
    def __init__(self,screen,ai_set):

        self.screen=screen
        #获取飞船的图片
        self.image=pygame.image.load('images\ship.bmp')
        #获取飞船图片和窗口的尺寸
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #设置飞船图片的位置
        self.rect.centerx= self.screen_rect.centerx
        self.rect.bottom= self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        #设置飞船的初始移动速度
        self.ship_speed=ai_set.ship_speed
        #飞船初始移动标志
        self.moving_right=False
        self.moving_left=False

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
    #飞船移动函数
    def moving(self):
        
        if self.moving_right:
            if self.rect.right<self.screen_rect.right:
                self.center+=self.ship_speed
            else:
                self.center=self.center
        
        if self.moving_left:
            if self.rect.left>0:
                self.center-=self.ship_speed
            else:
                self.center=self.center
        self.rect.centerx=self.center
    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx
