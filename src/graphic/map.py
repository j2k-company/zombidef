from random import random

from src.config import Tiles


class Map:
    def __init__(self):
        self.map = [[Tiles.void if random() > 0.5 else Tiles.base for _ in range(1000)] for _ in range(100)]

