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

    def _create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size if star.rect else (0,0)
        available_space_x = self.settings.screen_width - (star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = self.settings.screen.height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number=0, row_number=0):
        star = Star(self)
        star_width, star_height = star.rect.size if star.rect is not None else (0,0)
        star.x = star_width + 2 * star_width * star_number
        if star.rect is not None:
            star.rect.x = star.x
            star.rect.y = star_height + 2 * star_height * row_number
        self.stars.add(star)

        
if __name__ == '__main__':
    ai = StarGrid()
    ai.run_game()