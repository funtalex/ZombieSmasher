from src.utilities.my_functions import *
from src.game.game import Game


class Pause(Game):
    def run(self):
        while True:
            self.check_exit()
            keys = pygame.key.get_pressed()
            print_text('Pause. Press enter to continue.', 30, 200, 30, (255, 255, 255))
            if keys[pygame.K_RETURN]:
                return
            pygame.display.update()
            self.clock.tick(self.FPS)
