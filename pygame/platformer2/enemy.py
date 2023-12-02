import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/blob.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.direction
        self.move_counter += 1
        if self.move_counter > 100:
            self.direction *= -1
            self.move_counter *= -1