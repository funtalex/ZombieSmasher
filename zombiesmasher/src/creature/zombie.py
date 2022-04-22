from src.creature.creature import Creature


class Zombie(Creature):
    def __init__(self, x, y, height=70, width=101,
                 image_path='./images/objects/zombie.png', velocity=5):
        super().__init__(x, y, height, width, image_path, velocity)
