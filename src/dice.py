import random


class Dice:

    def __init__(self):
        self.throw = []

    def std_roll(self, num_throws: int):
        """
        Simulate rolling two standard six-sided dice.
        """
        self.throw = []
        for i in range(num_throws):
            self.throw.append(random.randint(1, 6))
        return self.throw

    def spec_roll(self):
        """
        Simulate rolling one user defined six-sided dice.
        """
        self.throw = []
        num_lst = [2, 4, 8, 16, 32, 64]
        self.throw.append(random.choice(num_lst))
        return self.throw
