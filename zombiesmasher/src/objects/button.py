from src.utilities.my_functions import *


class Button:
    def __init__(self, x, y, width, height, color, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.action = action

    def draw(self, message, font_size=30, text_color=(0, 0, 0)):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        print_text(message, self.x, self.y, font_size, text_color)

    def check_area(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        x = mouse[0]
        y = mouse[1]
        return click[0] == 1 and self.x < x < self.x + self.width and \
               self.y < y < self.y + self.height
