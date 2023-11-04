from pygame.sprite import Sprite
import pygame
vector = pygame.math.Vector2


class Player(Sprite):
    def __init__(self, x, y, grass_tile_group, water_main_tile_group):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.right_idle = []
        self.left_idle = []
        self.grass_tile_group = grass_tile_group
        self.water_main_tile_group = water_main_tile_group
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

        self.index = 0
        self.counter = 0
        self.direction = 1
        self.image = self.right_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 12

    def update(self):
        cooldown = 5
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)
        if self.counter > cooldown:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.right_images):
            self.index = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.counter += 1
            self.image = self.left_images[self.index]
            self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION

        elif keys[pygame.K_RIGHT]:
            self.direction = 1
            self.counter += 1
            self.image = self.right_images[self.index]
            self.acceleration.x = self.HORIZONTAL_ACCELERATION

        else:
            if self.direction == 1:
                self.counter += 1
                self.image = self.right_idle[self.index]
            elif self.direction == -1:
                self.counter += 1
                self.image = self.left_idle[self.index]
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity
        self.rect.bottomleft = self.position

        collided_platforms = pygame.sprite.spritecollide(
            self, self.grass_tile_group, False)
        if collided_platforms:
            print(self.velocity.y)
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top + 1
                self.velocity.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def jump(self):
        if pygame.sprite.spritecollide(self, self.grass_tile_group, False):
            self.velocity.y = - 1 * self.VERTICAL_JUMP_SPEED
