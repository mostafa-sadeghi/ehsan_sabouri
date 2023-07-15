import pygame
import random

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 5
COIN_ACCELERATION = 0.5

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font("AttackGraffiti.ttf", 32)


score_text = font.render(f"Score: {score}", True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)


title_text = font.render("Feed the dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH/2
title_rect.y = 10


lives_text = font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)


game_over_text = font.render("Game Over", True, DARKGREEN, GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

continue_text = font.render(
    "Press any key to continue...", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)


miss_sound = pygame.mixer.Sound("miss_sound.wav")
coin_sound = pygame.mixer.Sound("coin_sound.wav")
coin_sound.set_volume(.2)
miss_sound.set_volume(.2)

pygame.mixer.music.load("back_music.mp3")

player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT/2


coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.right = WINDOW_WIDTH + 50
coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 24)


pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 64:

        player_rect.y -= PLAYER_VELOCITY

    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:

        player_rect.y += PLAYER_VELOCITY

    if coin_rect.x <= 0:
        player_lives -= 1
        miss_sound.play()
        coin_rect.x = WINDOW_WIDTH + 50
        coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 24)
    else:
        coin_rect.x -= coin_velocity

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + 50
        coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 24)

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT/2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play()
                    is_paused = False

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    lives_text = font.render(f"Lives: {player_lives}", True, GREEN, DARKGREEN)
    score_text = font.render(f"Score: {score}", True, GREEN, DARKGREEN)

    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
