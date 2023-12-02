from pygame.sprite import Sprite
import pygame
from constants import *
class Player(Sprite):
    def __init__(self, x,y, enemy_group, lava_group):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.right_idle = []
        self.left_idle = []
        self.enemy_group = enemy_group
        self.lava_group = lava_group
        for i in range(1, 9):
            img = pygame.image.load(f"assets/boy/Run ({i}).png")
            img = pygame.transform.scale(img, (64, 64))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
            idle_img = pygame.image.load(f"assets/boy/Idle ({i}).png")
            idle_img = pygame.transform.scale(idle_img, (64, 64))
            self.right_idle.append(idle_img)
            idle_img = pygame.transform.flip(idle_img, True, False)
            self.left_idle.append(idle_img)
        idle_img = pygame.image.load(f"assets/boy/Idle ({i+1}).png")
        idle_img = pygame.transform.scale(idle_img, (64, 64))
        self.right_idle.append(idle_img)
        idle_img = pygame.transform.flip(idle_img, True, False)
        self.left_idle.append(idle_img)
        self.frame_index = 0
        self.counter = 0
        self.image = self.right_idle[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.idle = True
        self.inair = False
        self.dead_image = pygame.image.load("assets/ghost.png")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, tile_list, game_status):
        dx = 0
        dy = 0
        COOL_DOWN = 3
        if self.direction == 1:
            rect = pygame.Rect(self.rect.x + 15, self.rect.y+5, self.image.get_width()-30, self.image.get_height()-12)
        else:
            rect = pygame.Rect(self.rect.x + 10, self.rect.y+5, self.image.get_width()-30, self.image.get_height()-12)

        if game_status == "playing":
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and not self.jumped and not self.inair:
                self.vel_y = -15
                self.jumped = True
                self.inair = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                self.idle = False
                dx -= 5
                self.direction = -1
                self.counter += 1
            if key[pygame.K_RIGHT]:
                self.idle = False
                dx += 5
                self.direction = 1
                self.counter += 1
            
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                self.counter += 1
                self.idle = True



            if self.counter > COOL_DOWN:
                self.counter = 0
                self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
            if not self.idle:
                if self.direction == 1:
                    self.image = self.right_images[self.frame_index]
                if self.direction == -1:
                    self.image = self.left_images[self.frame_index]
            elif not self.jumped:
                if self.direction == 1:
                    self.image = self.right_idle[self.frame_index]
                if self.direction == -1:
                    self.image = self.left_idle[self.frame_index]
            else:
                if self.direction == 1:
                    self.image = self.right_images[1]
                if self.direction == -1:
                    self.image = self.left_images[1]

            #add gravity
            self.vel_y += 1
            dy += self.vel_y


            for tile in tile_list:
                if tile[1].colliderect(rect.x + dx, rect.y, self.image.get_width()-30, self.image.get_height()-12):
                    dx = 0
                if tile[1].colliderect(rect.x , rect.y + dy, self.image.get_width()-30, self.image.get_height()-12):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    else:
                        dy = tile[1].top - rect.bottom
                        self.vel_y = 0
                        self.inair = False

            if pygame.sprite.spritecollide(self, self.enemy_group, True)  :
                game_status = "gameover"



            self.rect.y += dy
            self.rect.x += dx
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

            return game_status

        elif game_status == "gameover":
            self.image = self.dead_image
            

        