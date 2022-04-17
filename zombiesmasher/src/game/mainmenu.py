from src.utilities.my_consts import *
from src.game.game import Game
from src.game.help import Help
from src.game.rungame import RunGame
from src.objects.button import Button


class MainMenu(Game):
    def run(self):
        self.set_buttons()
        while True:
            self.set_background('./images/background/background.jpg')
            self.draw_buttons()
            self.check_exit()
            self.check_button(self.button_array)
            pygame.display.update()
            self.clock.tick(self.FPS)

    def set_buttons(self):
        self.button_array.append(Button(200, 150, 80, 50, (255, 0, 34), self.start_game))
        self.button_array.append(Button(208, 250, 65, 50, (255, 0, 34), self.help_game))
        self.button_array.append(Button(208, 350, 65, 50, (255, 0, 34), quit))

    def draw_buttons(self):
        self.button_array[0].draw('Start')
        self.button_array[1].draw('Help')
        self.button_array[2].draw('Quit')

    @staticmethod
    def start_game():
        run_game = RunGame()
        run_game.run()

    @staticmethod
    def help_game():
        rules = Help()
        rules.run()

    button_array = []