from src.utilities.my_functions import *
from src.game.game import *


class GameOver(Game):
    def run(self, score):
        if score > Game.max_score:
            Game.max_score = score
        while True:
            self.set_background('./images/background/background.jpg')
            self.check_exit()
            if self.check_key():
                break
            print_text(f'Your score: {score}', 150, 100)
            print_text(f'Max score: {Game.max_score}', 150, 200)
            print_text('Press enter to go to main menu', 20, 300)
            pygame.display.update()
            self.clock.tick(self.FPS)

    @staticmethod
    def check_key():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False