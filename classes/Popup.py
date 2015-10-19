from livewires import games


class Popup(games.Text):
    dy = -2
    _dy = dy

    def update(self):
        if self.y <= 40:
            self.destroy()