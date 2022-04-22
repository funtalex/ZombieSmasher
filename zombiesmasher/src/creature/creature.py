from src.utilities.my_consts import *


class Creature:
    def __init__(self, x, y, height, width, image_path, velocity=5):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(image_path)
        self.velocity = velocity

    def move(self):
        self.y += self.velocity

    def draw(self):
        display.blit(self.image, (self.x, self.y))

    def in_display(self):
        return self.y > DISPLAY_HEIGHT

    def under_mouse(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            mouse = pygame.mouse.get_pos()
            if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
                return True
        return False
