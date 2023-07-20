import pygame
import random

pygame.init()

WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the clown")

FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1


score = 0
player_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY

clown_dx = random.choice([-1,1])
clown_dy = random.choice([-1,1])

BLUE = (1,175,209)
YELLOW = (248,231,28)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()
