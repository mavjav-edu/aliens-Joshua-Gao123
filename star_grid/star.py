import pygame
from pygame.sprite import Sprite
class Star(Sprite):
    SCALE_FACTOR=0.05
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("star_grid/star-vector-png-transparent-image-pngpix-21.png")
        # check if the image was loaded properly
        if self.image == None:
            print("Error loading image")
            exit()
        self.rect = self.image.get_rect()
        self.rect.x = self.SCALE_FACTOR*self.rect.width
        self.rect.y = self.SCALE_FACTOR*self.rect.height
        self.image = pygame.transform.scale(self.image,(self.rect.x,self.rect.y))
        print(f"Image is '{self.image.get_rect()}' large")
        self.x = 0
        self.y = float(self.rect.y)
