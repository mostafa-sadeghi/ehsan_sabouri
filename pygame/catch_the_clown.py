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

clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)

font = pygame.font.Font("Franxurter.ttf", 32)

title_text = font.render("catch the clown", False, BLUE)
title_text_rect = title_text.get_rect()
title_text_rect.topleft = (50, 10)

score_text = font.render(f"Score: {score}", False, YELLOW)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WINDOW_WIDTH - 150, 10)

lives_text = font.render(f"Lives: {player_lives}", False, YELLOW)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topleft = (WINDOW_WIDTH - 150, 50)

click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
background_sound = pygame.mixer.Sound("Bad Piggies Theme.mp3")

background_sound.set_volume(.4)

background_sound.play(-1)

background_image = pygame.image.load("background.png")
background_image_rect = background_image.get_rect()
background_image_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

clown_image = pygame.image.load("Clown.png")
clown_image_rect = clown_image.get_rect()
clown_image_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    display_surface.blit(background_image, background_image_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    display_surface.blit(clown_image, clown_image_rect)

    pygame.display.update()

pygame.quit()
