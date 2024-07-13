import datetime

from src.config import my_font
from src.exceptions import RealmNotFoundError, RegistrationEndedError, PlayerNotParticipatingInRound


class LobbyMenu:
    def __init__(self, app):
        self.app = app
        self.last_time = datetime.datetime.now()
        self.start_time = None
        self.message = ''

    def check_time(self):
        try:
            self.start_time = datetime.timedelta(seconds=self.app.client.participate()) + datetime.datetime.now()
        except RealmNotFoundError:
            self.start_time = None
            self.message = 'Ждем-с'
        except PlayerNotParticipatingInRound:
            self.start_time = None
            self.message = 'Ну че, мы не успели('
        except RegistrationEndedError:
            self.app.change_state()

    def update(self):
        if self.start_time:
            if datetime.datetime.now() >= self.start_time:
                self.app.change_state()
        if (datetime.datetime.now() - self.last_time).seconds > 2:
            self.last_time = datetime.datetime.now()
            self.check_time()

    def draw(self):
        if self.start_time:
            text_surface = my_font.render(f'Время до старта: {self.start_time - datetime.datetime.now()}', False,
                                          (255, 255, 255))
        else:
            text_surface = my_font.render(self.message, False, (255, 255, 255))
        self.app.screen.blit(text_surface, (0, 0))

    def run(self):
        self.update()
        self.draw()
