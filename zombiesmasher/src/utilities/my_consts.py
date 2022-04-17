import pygame

DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 600
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption('ZOMBIE SMASHER')
icon = pygame.image.load('./images/icon/head.jpg')
pygame.display.set_icon(icon)

max_score = 0