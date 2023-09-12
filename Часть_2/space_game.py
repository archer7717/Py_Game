import pygame
import sys
from gun import Gun
from controls import events
# Основной файл игры

def run():

    print("Запуск Игры")
    pygame.init()
    #Создание игровой области
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("КОСМО")
    # Цвет бэкграунда
    bg_color = (0,0,0)
    gun = Gun(screen)

    #Игровой цикл
    while True:
        # #обработка событий мышь,клава
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        events()
        screen.fill(bg_color)
        gun.output()
        #Прорисовка экрана
        pygame.display.flip()


run()
