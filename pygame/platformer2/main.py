import pygame
from constants import *
from world import World
from levels.level1 import world_data

from player import Player
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

world = World(world_data)

player = Player(100,screen_height-100)

bg_img = pygame.image.load("assets/sky.png")
sun_img = pygame.image.load("assets/sun.png")

def draw_grid():
    for i in range(14):
        pygame.draw.line(screen,(255,10,170), (0,i*50), (screen_width,i*50))
    for i in range(20):
        pygame.draw.line(screen,(255,10,170), (i*50,0), (i*50,screen_height))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    draw_grid()
    world.draw(screen)
    screen.blit(sun_img, (100,100))
    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

