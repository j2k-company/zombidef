from pygame import QUIT
from pygame.display import set_mode, flip, set_caption
from pygame.event import get
from pygame.time import Clock

from src.config import Settings, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.graphic.UI.lobby_manu import LobbyMenu
from src.graphic.game import Game
from src.network.client import Client


def main():
    app = App()
    app.run()


class App:
    def __init__(self):
        self.screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.events = None
        self.client = Client(Settings().token, test=True)
        # self.game_state = Game(self)
        self.game_state = LobbyMenu(self)

    def change_state(self):
        if isinstance(self.game_state, LobbyMenu):
            self.game_state = Game(self)
        elif isinstance(self.game_state, Game):
            self.game_state = LobbyMenu(self)

    def run(self):
        while True:
            flip()

            self.events = get()
            [exit() for event in self.events if event.type == QUIT]

            self.screen.fill((0, 0, 0))

            self.game_state.run()

            self.clock.tick(FPS)
            set_caption(f"FPS: {self.clock.get_fps() :.2f}")


if __name__ == "__main__":
    main()
