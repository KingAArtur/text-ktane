from random import choice

from .base_module import BombModule


class JustTypeItModule(BombModule):
    answer: str

    @classmethod
    def create(cls):
        module = cls()
        module.answer = choice(
            [
                'david mox',
                'David Mox',
                'DAVID MOX',
                'DAVID',
                'azaza david?'
            ]
        )
        return module

    def show(self) -> str:
        return 'I am pretty sure that you cannot repeat this: ' + f'**{self.answer}**'

    def guess(self, s: str) -> bool:
        if s == self.answer:
            self.disarm()
            return True
        else:
            return False
