import random
import pygame
from pygame.locals import *


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Burger Dog")

FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELERATION = 0.5

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font("assets/fonts/WashYourHand.ttf", 20)


points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render(f"Score: {score}", True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render(f"Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.midtop = (WINDOW_WIDTH / 2, 10)

eaten_text = font.render(f"Burgers Eaten: {burgers_eaten}", True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.midtop = (WINDOW_WIDTH / 2, 50)

lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)


bark_sound = pygame.mixer.Sound("assets/sounds/bark_sound.wav")
miss_sound = pygame.mixer.Sound("assets/sounds/miss_sound.wav")
pygame.mixer.music.load("assets/sounds/bd_background_music.wav")


left_dog_image = pygame.transform.scale(
    pygame.image.load("assets/images/dog.png"), (64, 64))
right_dog_image = pygame.transform.flip(left_dog_image, True, False)

player_image = right_dog_image
player_rect = player_image.get_rect()
player_rect.midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT)

burger_image = pygame.transform.scale(
    pygame.image.load("assets/images/burger.png"), (32, 32))
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 64), -100)

pygame.mixer.music.play(-1, 0.0)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = left_dog_image

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = right_dog_image

    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity

    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    if keys[pygame.K_SPACE] and boost_level > 0 and (keys[pygame.K_LEFT]
                                                     or keys[pygame.K_RIGHT]
                                                     or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1

    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    burger_points = (WINDOW_HEIGHT - burger_rect.y)//10 + 1

    burger_rect.y += burger_velocity

    if burger_rect.y > WINDOW_HEIGHT:
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 64), -100)
        miss_sound.play()
        player_lives -= 1
        burger_velocity = STARTING_BURGER_VELOCITY
        player_rect.centerx = WINDOW_WIDTH/2
        player_rect.bottom = WINDOW_HEIGHT

    if player_rect.colliderect(burger_rect):
        score += burger_points
        burgers_eaten += 1
        bark_sound.play()
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 64), -100)
        burger_velocity += BURGER_ACCELERATION

    boost_text = font.render(f"Boost: {boost_level}", True, ORANGE)
    points_text = font.render(f"Burger Points: {burger_points}", True, ORANGE)
    lives_text = font.render(f"Lives: {player_lives}", True, ORANGE)
    eaten_text = font.render(f"Burgers Eaten: {burgers_eaten}", True, ORANGE)
    score_text = font.render(f"Score: {score}", True, ORANGE)

    display_surface.fill(BLACK)
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
