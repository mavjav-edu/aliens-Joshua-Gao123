import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    SCALE_FACTOR = 0.15

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("star.png")

        # check if the image was loaded properly
        if self.image is None:
            print("Error loading image")
            exit()
        self.image = pygame.transform.scale(self.image,
            (
                self.SCALE_FACTOR * self.image.get_width(),
                self.SCALE_FACTOR * self.image.get_height()
            )
        )
        self.rect = self.image.get_rect()
        print(f"Image is '{self.image.get_rect()}' large")
        self.x = 0
        self.y = float(self.rect.y)
