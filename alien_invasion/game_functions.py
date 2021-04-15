import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship
from time import sleep

#按下按键
def check_keydown_event(event,ship,ai_set,bullets,screen):   
    if event.key==pygame.K_RIGHT:   #右键
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:   #左键
        ship.moving_left=True
    if event.key==pygame.K_SPACE:   #空格
        create_bullet(bullets,screen,ai_set,ship)
    if event.key==pygame.K_ESCAPE:   #退出键
        sys.exit()

#松开按键
def check_keyup_event(event,ship):   
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

#play_button按钮键
def check_play_button(stats,play_button,mouse_x,mouse_y,screen,ai_set,aliens,ship,bullets):
    if play_button.rect.collidepoint(mouse_x,mouse_y):   #按钮与鼠标碰撞
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active=True

        #清空外星人和子弹
        aliens.empty()
        bullets.empty()
        #创建新的外星人群，并让子弹居中
        create_fleet(screen,ai_set,aliens,ship)
        ship.center_ship()

def check_event(ship,ai_set,bullets,screen,stats,play_button,aliens):
    for event in pygame.event.get():
        #退出事件
        if event.type==pygame.QUIT:
            sys.exit()
        #鼠标事件
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()   #
            check_play_button(stats,play_button,mouse_x,mouse_y,screen,ai_set,aliens,ship,bullets)
        
        #键盘事件
        if event.type==pygame.KEYDOWN:  #按下按键
            check_keydown_event(event,ship,ai_set,bullets,screen)
        if event.type==pygame.KEYUP:    #松开按键
            check_keyup_event(event,ship)

#子弹的移动和消失
def update_bullet(bullets):   
    for bullet in bullets:
        bullet.y-=bullet.bullet_speed
        bullet.rect.y=bullet.y
        if bullet.rect.bottom<0:
            bullets.remove(bullet)

#创建子弹
def create_bullet(bullets,screen,ai_set,ship):   
    if len(bullets)<ai_set.bullet_number:   
        new_bullet=Bullet(screen,ai_set,ship)
        bullets.add(new_bullet)

#屏幕更新
def update_screen(ai_set,screen,ship,bullets,aliens,play_button,stats):
    screen.fill(ai_set.screen_bg_color)         #设置屏幕颜色
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()   #绘制飞船
    aliens.draw(screen)   #绘制外星人
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip()   #让最近绘制的屏幕可见

#创建外星人函数组
    #获取x方向外星人的个数
def get_alien_number_x(ai_set,alien_width):
    available_space_x=ai_set.screen_width-2*alien_width
    alien_number_x=int(available_space_x/(2*alien_width))
    return alien_number_x
    #获取y方向外星人的个数
def get_alien_number_y(ai_set,alien_height,ship):
    available_space_y=ai_set.screen_height-2*alien_height-7*ship.rect.height
    alien_number_y=int(available_space_y/(2*alien_height))
    return alien_number_y

    #创建外星人
def create_alien(screen,ai_set,number_x,number_y,aliens,alien_width,alien_height):
    alien=Alien(screen,ai_set)
    alien.x=alien_width*(1+2*number_x)
    alien.rect.x=alien.x
    alien.y=alien_height*(1+2*number_y)
    alien.rect.y=alien.y
    aliens.add(alien) 

    #创建外星人群
def create_fleet(screen,ai_set,aliens,ship):
    alien1=Alien(screen,ai_set)   #添加一个独立的飞船
    aliens.add(alien1)
    alien_width=alien1.rect.width
    alien_height=alien1.rect.height
    alien_number_x=get_alien_number_x(ai_set,alien_width) #调用函数
    alien_number_y=get_alien_number_y(ai_set,alien_height,ship) #调用函数
    aliens.remove(alien1)   #删除掉独立的飞船
    for number_x in range(alien_number_x):
        for number_y in range(alien_number_y):
            create_alien(screen,ai_set,number_x,number_y,aliens,alien_width,alien_height)#调用函数

#外星人向左右和向下移动          
def update_aliens(aliens,ai_set):
    for alien in aliens:
        alien.y+=ai_set.alien_speed_drop
        alien.rect.y=alien.y
        alien.check_direction()
        alien.update()

#碰撞事件
def collision_event(screen,bullets,aliens,ship,ai_set,stats):
    
    #子弹和外星人的碰撞
    collisons=pygame.sprite.groupcollide(bullets,aliens,True,True)   #元组与元组的碰撞
        #若外星人全部消失，则重新创建外星人群
    if len(aliens)==0:
        bullets.empty()
        create_fleet(screen,ai_set,aliens,ship)

    for alien in aliens:
        #外星人和飞船的碰撞以及外星人和屏幕底端的相撞
        if pygame.sprite.spritecollideany(ship,aliens) or alien.rect.bottom==ai_set.screen_height:
            if stats.ship_left>1:
                stats.ship_left-=1   #飞船数量减1
                bullets.empty()
                aliens.empty()
                ship.center_ship()   #将飞船居中
                sleep(3)
                break
            else:
                stats.game_active=False

#外星人移动
"""
def update_alien(aliens,ai_set,bullets,screen,ship):
    for alien in aliens:
        alien.y+=ai_set.alien_speed
        alien.rect.y=alien.y
        collisons=pygame.sprite.groupcollide(bullets,aliens,True,True)   #元组与元组的碰撞函数
    
        if pygame.sprite.spritecollideany(ship,aliens) or alien.rect.bottom==ai_set.screen_height:
            bullets.empty()
            aliens.empty()
            ship=Ship(screen,ai_set)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(screen,ai_set,aliens,ship)       
"""


















