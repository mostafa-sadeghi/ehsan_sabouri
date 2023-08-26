import pygame
from config import *
from player import Player

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.draw(display_surface)
    player_group.update()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
