import datetime

from pygame import KEYDOWN

from .camera import Camera
from .map import Map
from .player import Player
from ..config import CAMERA_CONTROL, my_font


class Game:
    def __init__(self, app):
        self.app = app
        self.map = Map()
        self.map.create_map(self.app.client.research_world().zpots)
        self.camera = Camera()
        self.player = Player(self.map)
        self.last_motion = datetime.datetime.now()
        self.lose = False

    def update_world(self):
        units = self.app.client.get_units()
        print(units)
        if units.player.game_ended_at is not None:
            self.lose = True
            return
        self.map.update_map(units)

    def update(self):
        for event in self.app.events:
            if event.type == KEYDOWN:
                if event.key in CAMERA_CONTROL:
                    self.camera.keyboard_control(event.key, self.map.max_dist)
                if event.key in PLAYER_CONTROL:
                    self.player.keyboard_control(event.key, self.camera.offset_x, self.camera.offset_y)

        if self.lose:
            return

        if (datetime.datetime.now() - self.last_motion).seconds >= 2:
            self.last_motion = datetime.datetime.now()
            if self.player.command_buffer:
                self.app.client.send_command(self.player.command_buffer)
            self.update_world()

    def draw(self):
        self.camera.custom_draw(self.app.screen, self.map.map)
        if self.lose:
            text_surface = my_font.render('Мы слили(', False, (255, 50, 50))
            self.app.screen.blit(text_surface, (0, 0))

    def run(self):
        self.update()
        self.draw()
