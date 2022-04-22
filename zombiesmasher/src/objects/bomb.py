from src.utilities.my_consts import *


class Bomb:
    def __init__(self, x=DISPLAY_WIDTH - 100, y=DISPLAY_HEIGHT // 2,
                 height=50, width=50,
                 image_path='./images/objects/bomb.png'):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(image_path)

    def under_mouse(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            mouse = pygame.mouse.get_pos()
            if self.x < mouse[0] < self.x + self.width and \
                    self.y < mouse[1] < self.y + self.height \
                    and self.is_available:
                self.is_available = False
                self.is_active = True
                clock = pygame.time.Clock()
                clock.tick(5)
                return True
        return False

    def draw_bomb(self):
        if self.is_available:
            display.blit(self.image, (self.x, self.y))

    is_available = True
    is_active = False
    AREA = 300
