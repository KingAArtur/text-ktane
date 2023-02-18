from random import choice

from .base_module import BombModule


class ChessModule(BombModule):
    answer: str
    board: str

    @classmethod
    def create(cls):
        module = cls()
        board, answer = choice(
            [
                ('7B/k1P5/3q4/8/8/8/8/7K w - - 0 1', 'c8=N'),
                ('3Q2QQ/8/PP4pp/PP4pk/RP6/7K/6P1/8 w - - 0 1', 'g4'),
                ('8/3k4/7p/6pP/1p4P1/1P6/Pr6/R3K3 w Q - 0 1', 'O-O-O'),
                ('8/kp6/pq6/p7/P2Q4/8/8/7K w - - 0 1', 'Qf2')
            ]
        )
        module.board = board
        module.answer = answer
        return module

    def show(self) -> str:
        return 'Why not play **chess** when you are to be exploded in a few minutes?\n\n' + f'`{self.board}`'

    def guess(self, s: str) -> bool:
        if s == self.answer:
            self.disarm()
            return True
        else:
            return False
