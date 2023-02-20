import sys
import pygame
from Settings import Settings
from Ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Inwazja!")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #sys.exit()
                #self.ship.blitme()

            pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.ship.blitme()
    def _update_screen(self):
        self.ship.blitme()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
