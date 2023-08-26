from random import randint
import pygame
from config import *
from monster import Monster
from player import Player

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)
monster_group = pygame.sprite.Group()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.warp()
    display_surface.fill((0, 0, 0))
    player_group.draw(display_surface)
    player_group.update()
    monster_group.draw(display_surface)
    monster_group.update()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
