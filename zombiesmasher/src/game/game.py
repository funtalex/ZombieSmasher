from src.utilities.my_consts import *
import sys


class Game:
    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    @staticmethod
    def check_exit():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    @staticmethod
    def check_button(button_array):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            for button in button_array:
                if button.check_area():
                    button.action()

    @staticmethod
    def set_background(image_path):
        display.blit(pygame.image.load(image_path), (0, 0))

    FPS = 60
    clock = pygame.time.Clock()
    score = 0
    max_score = 0
