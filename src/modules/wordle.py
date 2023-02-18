from random import choice
from collections import defaultdict
from typing import List

from .base_module import BombModule


def compare(guess: str, answer: str) -> str:
    if len(guess) != len(answer):
        return f'Length must be equal to {len(answer)}!'

    letters = defaultdict(int)
    for ch in answer:
        letters[ch] += 1

    response = ['-'] * len(guess)

    for i, ch in enumerate(guess):
        if ch == answer[i]:
            response[i] = '!'
            letters[ch] -= 1

    for i, ch in enumerate(guess):
        if ch != answer[i] and letters[ch] > 0:
            response[i] = '?'
            letters[ch] -= 1

    return ' '.join(response)


class WordleModule(BombModule):
    answer: str
    last_guesses: List[str]
    n_guesses: int
    max_guesses: int

    @classmethod
    def create(cls):
        module = cls()

        answer = choice(
            [
                'glyph',
                'baker',
                'wager',
                'frost',
                'unity',
                'chunk',
                'enemy'
            ]
        )

        module.answer = answer
        module.n_guesses = 0
        module.max_guesses = 6
        module.last_guesses = [r'\_ _ _ _ _']
        return module

    def show(self) -> str:
        desc = 'What do you think about it? ' + f'({self.n_guesses} / {self.max_guesses})'
        history = '\n\n'.join(self.last_guesses)
        return desc + '\n\n' + history

    def guess(self, s: str) -> bool:
        if s == self.answer:
            last_guess = s
            self.disarm()
        else:
            last_guess = f'{s}: {compare(s, self.answer)}'
        self.last_guesses.append(last_guess)

        self.n_guesses += 1
        if self.n_guesses > self.max_guesses:
            return False
        return True
