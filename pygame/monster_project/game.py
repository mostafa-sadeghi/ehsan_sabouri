from random import randint
import pygame

from config import WINDOW_WIDTH


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
