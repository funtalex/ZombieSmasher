from src.utilities.my_consts import *


def print_text(message, x, y, font_size=30, color=(255, 255, 255)):
    my_font = pygame.font.SysFont('Comic Sans MS', font_size)
    text = my_font.render(message, False, color)
    display.blit(text, (x, y))
