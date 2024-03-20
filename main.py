import pygame
#
import config

# Setup
pygame.init()
screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption(config.title)
pygame.display.set_icon(config.icon)
running = True

title = config.presstart_font.render("FOOD RAIN", True, (255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    screen.blit(title, (100, 300))
    pygame.display.flip()


pygame.quit()