from time import time
from typing import List
from enum import Enum
from random import shuffle

from src.modules import (
    BombModule,
    JustTypeItModule,
    ChessModule,
    CaesarModule,
    WordleModule,
    EquationModule,
    GuessNumberModule,
)


class BombState(Enum):
    WORKING = 0
    SOLVED = 1
    EXPLODED = 2


class Bomb:
    def __init__(self, *, strikes: int = 3, max_time: float = 300.0):
        self.max_strikes = strikes
        self.max_time = max_time

        self.strikes = 0
        self.start_time = time()
        self.remaining_time = max_time

        self.state = BombState.WORKING

        self.modules: List[BombModule] = [
            JustTypeItModule.create(),
            ChessModule.create(),
            CaesarModule.create(),
            WordleModule.create(),
            EquationModule.create(),
            GuessNumberModule.create()
        ]
        shuffle(self.modules)

    def get_remaining_time(self) -> float:
        if self.state == BombState.WORKING:
            self.remaining_time = max(self.max_time - (time() - self.start_time), 0.0)

        return self.remaining_time

    def check_if_solved(self):
        for module in self.modules:
            if not module.disarmed:
                return

        if self.state == BombState.WORKING:
            self.state = BombState.SOLVED

    def check_if_exploded(self):
        remaining_time = self.get_remaining_time()
        if self.strikes >= self.max_strikes or remaining_time == 0.0:
            if self.state == BombState.WORKING:
                self.state = BombState.EXPLODED

    def guess(self, module: BombModule, s: str):
        self.check_if_exploded()
        if self.state != BombState.WORKING:
            return

        try:
            result = module.guess(s)
        except ValueError:
            result = False

        if not result:
            self.strike()
        self.check_if_solved()

    def strike(self):
        self.strikes += 1
        self.check_if_exploded()
