from src.creature.creature import Creature


class Human(Creature):
    def __init__(self, x, y, height=95, width=73,
                 image_path='./images/objects/human.png', velocity=5):
        super().__init__(x, y, height, width, image_path, velocity)
