import pygame
from constants import *
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

bg_img = pygame.image.load("assets/sky.png")
sun_img = pygame.image.load("assets/sun.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))
    pygame.display.update()
    clock.tick(FPS)

