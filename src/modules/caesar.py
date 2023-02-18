from random import shuffle, randrange

from .base_module import BombModule


def shift_to_right(letter: str, dist: int) -> str:
    n = ord(letter) - ord('a')
    n = (n + dist) % 26
    return chr(ord('a') + n)


class CaesarModule(BombModule):
    answer: int
    letters: str

    @classmethod
    def create(cls):
        module = cls()

        answer = randrange(1, 26)
        letters = ['d', 'a', 'v', 'i', 'd']
        shuffle(letters)
        for i, ch in enumerate(letters):
            letters[i] = shift_to_right(ch, answer)

        module.letters = ''.join(letters)
        module.answer = answer
        return module

    def show(self) -> str:
        return 'Imagine using **CAESAR CIPHER** in bomb, ' + f'**{self.letters}**'

    def guess(self, s: str) -> bool:
        if int(s) == self.answer:
            self.disarm()
            return True
        else:
            return False
