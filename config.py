import pygame

pygame.init()

#
title = "FOOD RAIN"
icon = pygame.image.load("assets/img/broccoli.png")

# Screen values
screen_width = 350
screen_height = 660

# Fonts
## Press start 2p
presstart_path = "assets/fonts/presstart.ttf"
presstart_size = 16
presstart_font = pygame.font.Font(presstart_path, presstart_size)