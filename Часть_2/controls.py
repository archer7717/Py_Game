import pygame,sys

def events():
    #обработка событий мышь,клава
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        