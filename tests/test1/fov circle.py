import pygame
import os


image_path = "circle.png"


pygame.init()


image = pygame.image.load(image_path)
screen_width, screen_height = image.get_size()


os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'


window = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.SRCALPHA)


image = image.convert_alpha()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    window.fill((0, 0, 0, 0))

   
    window.blit(image, (0, 0))

   
    pygame.display.flip()

pygame.quit()
