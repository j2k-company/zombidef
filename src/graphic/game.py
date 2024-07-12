from pygame import KEYDOWN

from .camera import Camera
from .map import Map
from ..config import CAMERA_CONTROL


class Game:
    def __init__(self, app):
        self.app = app
        self.map = Map()
        self.camera = Camera()

    def update(self):
        for event in self.app.events:
            if event.type == KEYDOWN:
                if event.key in CAMERA_CONTROL:
                    self.camera.keyboard_control(event.key)

    def draw(self):
        self.camera.custom_draw(self.app.screen, self.map.map)

    def run(self):
        self.update()
        self.draw()
