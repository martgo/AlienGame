import pygame
import Settings

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Pics/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed
            #self.rect.x+=1
        if self.moving_left:
            self.x -= self.settings.ship_speed
            #self.rect.x-=1

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)