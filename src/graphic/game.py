from .map import Map


class Game:
    def __init__(self, app):
        self.app = app
        self.map = Map()

    def update(self):
        pass

    def draw(self):
        self.map.draw(self.app.screen)

    def run(self):
        self.update()
        self.draw()
