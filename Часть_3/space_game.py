import pygame, controls
from gun import Gun
from pygame.sprite import Group

# Основной файл игры

def run():

    print("Запуск Игры")
    pygame.init()
    #Создание игровой области
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("КОСМО")
    # Цвет бэкграунда
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group() #список

    #Добавление музыки
    # pygame.mixer.music.load("Часть_2/sound/background.ogg")
    # pygame.mixer.music.play()
    #Игровой цикл
    while True:
        controls.events(screen, gun, bullets)    # обрабатываем события нажатия клавиш ставим True или False
        gun.update_gun()        # если клавиша нажата смещаем космо аппарат
        controls.update(screen,gun,bg_color,bullets)
        controls.update_bullets(bullets)


run()
