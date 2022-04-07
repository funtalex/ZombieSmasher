import sys
import pygame
import random

pygame.init()

display_width = 480
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('ZOMBIE SMASHER')
icon = pygame.image.load(r'./images/icon/head.jpg')
pygame.display.set_icon(icon)

max_score = 0


def print_text(message, x, y, font_size=30, color=(0, 0, 0)):
    my_font = pygame.font.SysFont('Comic Sans MS', font_size)
    text = my_font.render(message, False, color)
    display.blit(text, (x, y))
    pygame.display.update()


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

    def check_area(self, x, y):
        return self.x < x < self.x + self.width and self.y < y < self.y + self.height


class Bomb:
    def __init__(self, x=display_width - 100, y=display_height // 2,
                 height=50, width=50,
                 image=pygame.image.load(r'./images/objects/bomb.png')):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = image

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
    area = 200



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
                if button.check_area(mouse[0], mouse[1]):
                    button.action()

    @staticmethod
    def set_background(image):
        display.blit(image, (0, 0))

    FPS = 60
    clock = pygame.time.Clock()
    score = 0
    max_score = 0


class MainMenu(Game):
    def run(self):
        self.set_buttons()
        while True:
            self.set_background(pygame.image.load(r'./images/background/background.jpg'))
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


class RunGame(Game):
    def run(self):
        self.zombie_array = []
        self.health = self.max_health
        self.score = 0
        self.bomb.is_active = False
        self.bomb.is_available = True
        while True:
            self.set_background(pygame.image.load(r'./images/background/background.jpg'))
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
        x = random.randrange(0, display_width - 100)
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
        image = pygame.image.load(r'./images/objects/heart.png')
        x = display_width - 200
        y = 30
        for i in range(self.health):
            display.blit(image, (x, y))
            x += 60

    def kill(self, zombie):
        image = pygame.image.load(r'./images/objects/dead.png')
        display.blit(image, (zombie.x, zombie.y))
        pygame.display.update()
        self.score += 1
        self.zombie_array.remove(zombie)

    def in_bomb(self, zombie):
        mouse = pygame.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
        if x - Bomb.area <= zombie.x <= x + Bomb.area and y - Bomb.area <= zombie.y <= y + Bomb.area:
            return True
        return False

    def kill_area(self):
        image = pygame.image.load(r'./images/objects/boom.png')
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

    max_health = 3
    health = 3
    zombie_array = []
    bomb = Bomb()


class Pause(Game):
    def run(self):
        while True:
            self.check_exit()
            keys = pygame.key.get_pressed()
            print_text('Pause. Press enter to continue.', 30, 200)
            if keys[pygame.K_RETURN]:
                return
            pygame.display.update()
            self.clock.tick(self.FPS)


class Help(Game):
    def run(self):
        while True:
            self.set_background(pygame.image.load(r'./images/background/background.jpg'))
            self.print_rules()
            self.check_exit()
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


class GameOver(Game):
    def run(self, score):
        if score > Game.max_score:
            Game.max_score = score
        while True:
            self.set_background(pygame.image.load(r'./images/background/background.jpg'))
            self.check_exit()
            if self.check_key():
                break
            print_text(f'Your score: {score}', 150, 100)
            print_text(f'Max score: {Game.max_score}', 150, 200)
            print_text('Press enter to go to main menu', 20, 300)
            self.clock.tick(self.FPS)

    @staticmethod
    def check_key():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        return False


class Creature:
    def __init__(self, x, y, height, width, image, velocity=5):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = image
        self.velocity = velocity

    def move(self):
        self.y += self.velocity

    def draw(self):
        display.blit(self.image, (self.x, self.y))

    def in_display(self):
        return self.y > display_height

    def under_mouse(self):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            mouse = pygame.mouse.get_pos()
            if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
                return True
        return False




class Human(Creature):
    def __init__(self, x, y, height=95, width=73,
                 image=pygame.image.load(r'./images/objects/human.png'), velocity=5):
        super().__init__(x, y, height, width, image, velocity)



class Zombie(Creature):
    def __init__(self, x, y, height=70, width=101,
                 image=pygame.image.load(r'./images/objects/zombie.png'), velocity=5):
        super().__init__(x, y, height, width, image, velocity)


main_menu = MainMenu()
main_menu.run()
