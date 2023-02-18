from random import randrange, choice
from typing import List

from .base_module import BombModule


class GuessNumberModule(BombModule):
    answer: int
    last_guesses: List[str]

    max_number: int
    n_guesses: int
    max_guesses: int

    @classmethod
    def create(cls):
        module = cls()

        max_number = 100
        max_guesses = 7

        answer = randrange(1, max_number + 1)

        module.answer = answer
        module.last_guesses = []
        module.max_number = max_number
        module.n_guesses = 0
        module.max_guesses = max_guesses
        return module

    def show(self) -> str:
        desc = f'Just guess a number from 1 to {self.max_number}! Attempt {self.n_guesses} / {self.max_guesses}'
        history = '\n\n'.join(self.last_guesses)
        return desc + '\n\n' + history

    def guess(self, s: str) -> bool:
        s = int(s)
        if s == self.answer:
            last_guess = f'{s}? Correct!'
            self.disarm()
        else:
            if s > self.answer:
                last_guess = choice(
                    [
                        f'{s}? Your number is bigger!',
                        f'{s}? My number is smaller!'
                    ]
                )
            else:
                last_guess = choice(
                    [
                        f'{s}? Your number is smaller!',
                        f'{s}? My number is bigger!'
                    ]
                )
        self.last_guesses.append(last_guess)

        self.n_guesses += 1
        if self.n_guesses > self.max_guesses:
            return False
        return True
