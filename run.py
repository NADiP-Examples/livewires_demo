from livewires import games, color
from classes.Hero import Hero
from classes.Game_objects import Monster, Plant
from classes.Popup import Popup


def keypress(key):
    unit.key_press(key)

# MAIN
games.init(screen_width=640, screen_height=480, fps=30)

games.screen.keypress = keypress

games.screen.add(Monster(x=60))
games.screen.add(Monster(x=120))
games.screen.add(Plant(x=180))
games.screen.add(Plant(x=220))

unit = Hero(x=40)
unit.set_popup(Popup)
games.screen.add(unit)
games.screen.add(games.Text(value='Движение: A - влево, D - вправо',
                            size=25, color=color.red, x=100, y=350, left=True, is_collideable=False))
games.screen.add(games.Text(value='"Пробел" - чтобы увидеть типы объектов с которыми пересекаетесь',
                            size=25, color=color.red, x=100, y=400, left=True, is_collideable=False))

games.screen.mainloop()