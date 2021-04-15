import pygame.font

class Button():
    def __init__(self,ai_set,screen,msg):
        #初始化按钮的属性
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #设置按钮的属性
        self.width,self.height=200,50
        self.color=(255,255,255)
        self.text_color=(0,0,0)
        self.font=pygame.font.SysFont(None,48)   #字体

        #创建按钮
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        #按钮只需创建一次
        self.prep_msg(msg)   #调用函数prep_msg()
    def prep_msg(self,msg):
        #msg为输入文本，将msg渲染成图像并放在button的中间
        #self.font.render(文本内容，True,文字颜色，文本框填充颜色)
        self.msg_image=self.font.render(msg,True,self.text_color,self.color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        #先绘制按钮，再绘制文本
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
