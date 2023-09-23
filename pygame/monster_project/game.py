from random import choice, randint
import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from monster import Monster


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0

        self.round_time = 0

        self.player = player
        self.monster_group = monster_group

        self.next_level_sound = pygame.mixer.Sound("assets/next_level.wav")
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")
        self.target_monster_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]

        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WINDOW_WIDTH/2
        self.target_monster_rect.top = 30

        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")

    def draw(self, display_surface):
        COLORS = ((20, 176, 235), (87, 201, 47),
                  (226, 73, 243), (243, 157, 20))
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        player_lives = self.font.render(
            f"Lives: {self.player.lives}", True, (255, 255, 255))
        player_lives_rect = player_lives.get_rect()
        player_lives_rect.topright = (WINDOW_WIDTH, 5)

        pygame.draw.rect(
            display_surface, COLORS[self.target_monster_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 8)

        display_surface.blit(score_text, score_rect)
        display_surface.blit(player_lives, player_lives_rect)
        display_surface.blit(self.target_monster_image,
                             self.target_monster_rect)

    def update(self, display_surface, running):
        self.check_collisions(display_surface, running)

    def check_collisions(self, display_surface, running):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 100 * self.round_number
                collided_monster.remove(self.monster_group)
                if self.monster_group:
                    self.catch_sound.play()
                    self.choose_new_target()
                else:
                    self.player.reset()
                    self.start_new_round()

            else:
                self.player.lives -= 1
                self.player.reset()
                if self.player.lives <= 0:
                    self.pause_game(
                        f"Final Score:{self.score}", "Press 'Enter' to play again", display_surface, running)
                    self.reset_game()

    def pause_game(self, main_text, sub_text, display_surface, running):
        main_text = self.font.render(main_text, True, (255, 255, 255))
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        sub_text = self.font.render(sub_text, True, (255, 255, 255))
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 64)
        display_surface.fill((0, 0, 0))
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False

                if event.type == pygame.QUIT:
                    running = False
                    is_paused = False

    def reset_game(self):
        self.score = 0
        self.round_number = 0
        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()

        self.start_new_round()

    def choose_new_target(self):
        target_monster = choice(self.monster_group.sprites())
        self.target_monster_image = target_monster.image
        self.target_monster_type = target_monster.type

    def start_new_round(self):
        self.round_number += 1
        self.round_time = 0
        for i in range(self.round_number):
            self.monster_group.add(Monster(randint(0, WINDOW_WIDTH-64),
                                           randint(100, WINDOW_HEIGHT-164),
                                           self.target_monster_images[0], 0))
            self.monster_group.add(Monster(randint(0, WINDOW_WIDTH-64),
                                           randint(100, WINDOW_HEIGHT-164),
                                           self.target_monster_images[1], 1))
            self.monster_group.add(Monster(randint(0, WINDOW_WIDTH-64),
                                           randint(100, WINDOW_HEIGHT-164),
                                           self.target_monster_images[2], 2))
            self.monster_group.add(Monster(randint(0, WINDOW_WIDTH-64),
                                           randint(100, WINDOW_HEIGHT-164),
                                           self.target_monster_images[3], 3))
