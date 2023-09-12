import pygame,sys
from bullet import Bullet

def events(screen, gun, bullets):
    #обработка событий мышь,клава
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:      # нажал на клаву
            if event.key == pygame.K_d:         # в право
                gun.mright = True               
            if event.key == pygame.K_a:         # в лево
                gun.mleft = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen,gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:        # отжал  клаву
            if event.key ==  pygame.K_d:        # в право
                gun.mright = False
            if event.key ==  pygame.K_a:        # в лево
                gun.mleft = False   

def update(screen, gun, bg_color, bullets):
        screen.fill(bg_color)

        for bullet in bullets.sprites():
            bullet.draw_bullet()

        gun.output()
        #Прорисовка экрана
        pygame.display.flip()

def update_bullets(bullets):
    """Обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))

