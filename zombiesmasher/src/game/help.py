from src.utilities.my_functions import *
from src.game.game import Game
from src.objects.button import Button


class Help(Game):
    def run(self):
        is_running = True
        back_button = Button(100, 450, 300, 50, (250, 0, 0), None)
        while (is_running):
            self.set_background('./images/background/background.jpg')
            self.print_rules()
            self.check_exit()
            back_button.draw("GO TO MAIN MENU")
            is_running = not back_button.check_area()
            if self.check_key():
                break
            pygame.display.update()
            self.clock.tick(self.FPS)

    @staticmethod
    def print_rules():
        print_text('How to play', 50, 50, 60)
        print_text('Click on Zombie to kill it', 20, 150)
        print_text('If you kill human or miss zombie ', 20, 250)
        print_text('3 times game will be over', 20, 300)

    def check_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        return False