import pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Second Game")
GREEN = (0,255,0)
DARKGREEN = (10,50,10)
BLACK = (0,0,0)

sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")

sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(0.1)
sound_2.play()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1,0.0)

pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()
fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)
system_font = pygame.font.SysFont('calibri',64)
custom_font = pygame.font.Font('AttackGraffiti.ttf', 32)
system_text = system_font.render("Dragon Game", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


custom_text = custom_font.render("Moving The dragon", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT // 2 + 100)

dragon_left_image = pygame.image.load("images/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load("images/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.draw.line(display_surface, (255, 255, 255),
                     (0, 75), (WINDOW_WIDTH, 75), 4)
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    pygame.display.update()


pygame.quit()
