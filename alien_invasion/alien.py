from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    def __init__(self,screen,ai_set):
        super().__init__()
        self.screen=screen
        self.ai_set=ai_set
        #获取外星人的图片和屏幕的尺寸
        self.image=pygame.image.load('images\waixingren.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #设置外星人的位置
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

        self.direction=1
        
    def check_direction(self):
        if self.rect.right>=self.screen_rect.width or self.rect.left<=0:
            self.direction=-self.direction
            self.y+=self.rect.height
            self.rect.y=self.y

            

    def update(self):
        self.x+=self.ai_set.alien_speed_factor*self.direction
        self.rect.x=self.x


    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
