from random import randrange
from itertools import product
from collections import defaultdict

from .base_module import BombModule


def generate_equation(degree: int, root: int) -> str:
    roots = []
    for _ in range(degree - 1):
        roots.append(randrange(-10, 0))
    roots.append(root)

    roots_with_x = [('x', root) for root in roots]
    equation = [0] * (degree + 1)
    for combination in product(*roots_with_x):
        coefficient = 1
        deg = 0
        for elem in combination:
            if elem == 'x':
                deg += 1
            else:
                coefficient *= -elem

        equation[deg] += coefficient

    return ' + '.join(reversed([
        f'{coefficient if coefficient != 1 else ""}' + (f'x^{deg}' if deg > 1 else ('x' if deg == 1 else ''))
        for deg, coefficient in enumerate(equation)
    ])).replace('+ -', '- ') + ' = 0'


class EquationModule(BombModule):
    answer: int
    equation: str
    degree: int

    @classmethod
    def create(cls):
        module = cls()

        degree = 4
        answer = randrange(1, 10)
        equation = generate_equation(degree, answer)

        module.answer = answer
        module.equation = equation
        module.degree = degree
        return module

    def show(self) -> str:
        return f'This equation of {self.degree} degree is unsolvable. Good luck!\n\n' + self.equation

    def guess(self, s: str) -> bool:
        if int(s) == self.answer:
            self.disarm()
            return True
        else:
            return False
