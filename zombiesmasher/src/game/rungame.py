import random
from src.utilities.my_functions import *
from src.game.game import Game
from src.game.gameover import GameOver
from src.game.pause import Pause
from src.creature.human import Human
from src.creature.zombie import Zombie
from src.objects.bomb import Bomb


class RunGame(Game):
    def run(self):
        self.zombie_array = []
        self.health = self.MAX_HEALTH
        self.score = 0
        self.bomb.is_active = False
        self.bomb.is_available = True
        while True:
            self.set_background('./images/background/background.jpg')
            self.check_exit()
            self.check_keys()
            self.check_mouse()
            self.check_runaway()
            self.move_zombies()
            self.draw_zombies()
            self.add_zombies()
            self.print_score()
            if self.health <= 0:
                break
            self.print_health()

            self.bomb.draw_bomb()
            pygame.display.update()
            self.clock.tick(self.FPS)
        game_over = GameOver()
        game_over.run(self.score)

    def move_zombies(self):
        for zombie in self.zombie_array:
            zombie.move()

    def draw_zombies(self):
        for zombie in self.zombie_array:
            zombie.draw()

    def add_zombies(self):
        if len(self.zombie_array) < 15:
            choice = random.randrange(0, 5)
            if choice == 0:
                new_creature = self.make_human()
            else:
                new_creature = self.make_zombie()
            self.zombie_array.append(new_creature)

    def find_coord(self):
        x = random.randrange(0, DISPLAY_WIDTH - 100)
        if len(self.zombie_array) == 0:
            y = -100
        else:
            y = min(0, min(self.zombie_array, key=lambda t: t.y).y)
        y -= random.randrange(50, 500)
        return x, y

    def make_human(self):
        x, y = self.find_coord()
        return Human(x, y)

    def make_zombie(self):
        x, y = self.find_coord()
        return Zombie(x, y)

    def check_runaway(self):
        for zombie in self.zombie_array:
            if zombie.in_display():
                if type(zombie).__name__ == 'Zombie':
                    self.health -= 1
                self.zombie_array.remove(zombie)

    def print_score(self):
        print_text(f'Score: {self.score}', 20, 30, 30, (255, 255, 255))

    @staticmethod
    def check_keys():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause = Pause()
            pause.run()

    def print_health(self):
        image = pygame.image.load('./images/objects/heart.png')
        x = DISPLAY_WIDTH - 200
        y = 30
        for i in range(self.health):
            display.blit(image, (x, y))
            x += 60

    def kill(self, zombie):
        image = pygame.image.load('./images/objects/dead.png')
        display.blit(image, (zombie.x, zombie.y))
        pygame.display.update()
        self.score += 1
        self.zombie_array.remove(zombie)

    def in_bomb(self, zombie):
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
        if x - Bomb.AREA <= zombie.x <= x + Bomb.AREA and y - Bomb.AREA <= zombie.y <= y + Bomb.AREA:
            return True
        return False

    def kill_area(self):
        image = pygame.image.load('./images/objects/boom.png')
        mouse = pygame.mouse.get_pos()
        display.blit(image, (mouse[0] - 150, mouse[1] - 150))
        pygame.display.update()
        for zombie in self.zombie_array:
            if type(zombie).__name__ == 'Zombie' and self.in_bomb(zombie):
                self.kill(zombie)

    def check_mouse(self):
        click = pygame.mouse.get_pressed()

        if self.bomb.is_active and click[0] == 1:
            self.bomb.is_active = False
            self.kill_area()

        self.bomb.under_mouse()

        for zombie in self.zombie_array:
            if zombie.under_mouse():
                if type(zombie).__name__ == 'Zombie':
                    self.kill(zombie)
                else:
                    self.health -= 3
                break

    MAX_HEALTH = 3
    health = 3
    zombie_array = []
    bomb = Bomb()