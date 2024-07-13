import datetime

from pygame import KEYDOWN

from .camera import Camera
from .map import Map
from .player import Player
from ..config import CAMERA_CONTROL


class Game:
    def __init__(self, app):
        self.app = app
        self.map = Map()
        self.map.create_map(self.app.client.research_world())
        self.camera = Camera()
        self.player = Player(self.map)
        self.last_motion = datetime.datetime.now()

    def update_world(self):
        units = self.app.client.get_units()
        self.map.update_map(units)

    def update(self):
        if (datetime.datetime.now() - self.last_motion).seconds >= 2:
            self.last_motion = datetime.datetime.now()
            if self.player.command_buffer:
                self.app.client.send_command(self.player.command_buffer)
            self.update_world()

        for event in self.app.events:
            if event.type == KEYDOWN:
                if event.key in CAMERA_CONTROL:
                    self.camera.keyboard_control(event.key)

    def draw(self):
        self.camera.custom_draw(self.app.screen, self.map.map)

    def run(self):
        self.update()
        self.draw()
