import os
import settings

from pygame import *
from livewires import games, color


class Hero(games.Sprite):
    """
    Герой - главный персонаж игры
    """
    type = 'hero'  # Герою тип ни к чему, но я просто указал по аналогии с другими объектами
    speed = 2
    popup_class = None

    def __init__(self, x=100, y=200):
        self.img = games.load_image(os.path.join(settings.IMG_DIR, 'hero.png'))
        self.img = transform.scale(self.img, (40, 40))
        super(Hero, self).__init__(image=self.img, x=x, y=y, dx=0, dy=0, angle=0, is_collideable=True)

    def update(self):
        self.move()

    def move(self):
        if games.keyboard.is_pressed(games.K_d):
            self.dx = self.speed
        elif games.keyboard.is_pressed(games.K_a):
            self.dx = -self.speed
        else:
            self.dx = 0

    def set_popup(self, popup_class):
        """
        Устанавливает класс для всплывающего текста
        """
        self.popup_class = popup_class

    def popup(self):
        """
        Создает всплывающий текст
        """
        # obj.type - возвращает тип объекта. Obj - это один из объектов, с которым мы пересекаемся на момент проверки
        value = ' - '.join([obj.type for obj in self.overlapping_sprites])   # тут немного сложный код
        # Но в нем не сложно разобраться, если погуглить как работает каждая его часть

        if self.popup_class:
            games.screen.add(self.popup_class(value=value, size=20, color=color.blue, x=self.x, y=self.y - 40))

    def key_press(self, key):
        """
        Вызывается каждый раз при НАЖАТИИ любой клавиши
        """
        if key == K_SPACE:
            self.popup()
