import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from gamestats import Gamestats
from button import Button


def run_game():
    #初始化游戏并创建一个游戏对象
    pygame.init()             #初始化背景设置
    pygame.display.set_caption('alien_invasion')     #创建标题
    ai_set=Settings()          #设置的类
    screen=pygame.display.set_mode((ai_set.screen_width,ai_set.screen_height))  #设置游戏窗口的大小

    play_button=Button(ai_set,screen,'Play')   #创建一个按钮
    ship=Ship(screen,ai_set)   #创建一个飞船
    bullets=Group()   #创建一个子弹组
    aliens=Group()    #创建外星人组
    stats=Gamestats(ai_set)
    
    gf.create_fleet(screen,ai_set,aliens,ship)  #创建外星人群
    

    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_event(ship,ai_set,bullets,screen,stats,play_button,aliens)
        if stats.game_active:
            ship.moving()   #飞船的移动
            gf.update_bullet(bullets)   #子弹的移动
            gf.update_aliens(aliens,ai_set)   #外星人的移动
            gf.collision_event(screen,bullets,aliens,ship,ai_set,stats)

        #屏幕刷新
        gf.update_screen(ai_set,screen,ship,bullets,aliens,play_button,stats)
      
run_game()
