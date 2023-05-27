import pygame
import os
import sys
pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''
print(wd)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
icon_image = pygame.image.load(os.path.join(
    wd, 'images', "watermelon.png")).convert_alpha()
pygame.display.set_icon(icon_image)
pygame.display.set_caption("Our First Game in pygame!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
display_surface.fill(BLUE)

pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 7)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 7)

pygame.draw.circle(display_surface, WHITE,
                   (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW,
                   (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0)

pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

# the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
