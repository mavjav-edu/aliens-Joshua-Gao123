import pygame
from star import Star
class StarGrid:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Stars")
        self.stars = pygame.sprite.Group()        
        self._create_star()
    def _update_screen(self):
        self.screen.fill((50, 50, 200))
        self.stars.draw(self.screen)
        pygame.display.flip()
    def run_game(self):
        while True:
            self._update_screen()

    def _create_star(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height
        self.stars.add(star)

        
if __name__ == '__main__':
    ai = StarGrid()
    ai.run_game()