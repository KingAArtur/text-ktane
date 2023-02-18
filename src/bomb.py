from time import time
from typing import List

from src.modules import BombModule, JustTypeItModule, ChessModule, CaesarModule, WordleModule


class Bomb:
    def __init__(self, *, strikes: int = 3, max_time: float = 300.0):
        self.max_strikes = strikes
        self.max_time = max_time

        self.strikes = 0
        self.time = time()

        self.solved = False
        self.exploded = False

        self.modules: List[BombModule] = [
            JustTypeItModule.create(),
            ChessModule.create(),
            CaesarModule.create(),
            WordleModule.create()
        ]

    def check_if_solved(self):
        for module in self.modules:
            if not module.disarmed:
                return

        self.solved = True

    def get_remaining_time(self) -> float:
        current_time = time()
        return max(self.max_time - (current_time - self.time), 0.0)

    def check_if_exploded(self):
        remaining_time = self.get_remaining_time()
        if self.strikes >= self.max_strikes or remaining_time == 0.0:
            self.exploded = True

    def guess(self, module: BombModule, s: str):
        result = module.guess(s)
        if not result:
            self.strike()
        self.check_if_solved()

    def strike(self):
        self.strikes += 1
        self.check_if_exploded()
