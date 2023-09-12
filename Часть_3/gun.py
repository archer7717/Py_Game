import pygame

class Gun():
    def __init__(self,screen):
        # создание пушки

        self.screen = screen
        self.image = pygame.image.load('image/space.png')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.mright = False     #Добавить
        self.mleft = False     #Добавить
        self.speed = 1.5

    def output(self):
        #отрисовка пушки
        self.screen.blit(self.image,self.rect)
    
    def update_gun(self):
        """Обновление позиции"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += self.speed

        if self.mleft and  self.rect.left > 0:
            self.center -= self.speed  

        self.rect.centerx = self.center