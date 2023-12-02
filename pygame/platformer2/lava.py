import pygame
from pygame.sprite import Sprite
from constants import *

class Lava(Sprite):
    def __init__(self,x,y):
        super().__init__()
        img = pygame.image.load("assets/lava.png")
        self.image = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE/2))
        self.rect = self.image.get_rect(bottomleft=(x,y))