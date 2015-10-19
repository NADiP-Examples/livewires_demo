import os
from pygame import *
from livewires import games, color
import settings

"""
Классы Монстра и Растения довльно маленькие,
в этом случае ни к чему их разносить по разным файлам
"""


class Monster(games.Sprite):
    """
    Если назначение класс очевидно из его названия, и класс не сложный, то комментарии можно опустить
    """
    type = 'monster'  # Тут задаем тип объекта, чтобы отличить Монстра от прочих игровых объектов
    change_x = 0
    speed = 0.5
    move_zone = 40

    def __init__(self, x=100, y=200):
        img = games.load_image(os.path.join(settings.IMG_DIR, 'monster.png'))
        img = transform.scale(img, (40, 40))
        super(Monster, self).__init__(image=img, x=x, y=y, dx=-self.speed, dy=0, angle=0, is_collideable=True)

    def update(self):
        self.auto_move()

    def auto_move(self):
        self.change_x += self.dx
        if self.change_x < -self.move_zone:
            self.dx = self.speed
        elif self.change_x > self.move_zone:
            self.dx = -self.speed


class Plant(games.Sprite):
    type = 'plant'  # Аналогично задаем тип Растению

    def __init__(self, x=100, y=200):
        self.img = games.load_image(os.path.join(settings.IMG_DIR, 'plant.png'))
        self.img = transform.scale(self.img, (40, 40))
        super(Plant, self).__init__(image=self.img, x=x, y=y, dx=0, dy=0, angle=0, is_collideable=True)