from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.right_idle = []
        self.left_idle = []
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
        self.image = self.right_idle[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,10,210), self.rect, 2)

    def update(self):
        dx = 0
        dy = 0

        #add gravity
        self.vel_y += 1

        dy += self.vel_y
        self.rect.y += dy

        # TODO ###################################

