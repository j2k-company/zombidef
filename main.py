from pygame import QUIT
from pygame.display import set_mode, flip, set_caption
from pygame.event import get
from pygame.time import Clock

from src.config import Settings, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.graphic.game import Game


def main():
    print(Settings())
    app = App()
    app.run()


class App:
    def __init__(self):
        self.screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.events = None
        self.game = Game(self)

    def run(self):
        while True:
            flip()

            self.events = get()
            [exit() for event in self.events if event.type == QUIT]

            self.screen.fill((0, 0, 0))

            self.game.run()

            self.clock.tick(FPS)
            set_caption(f"FPS: {self.clock.get_fps() :.2f}")


if __name__ == "__main__":
    main()
