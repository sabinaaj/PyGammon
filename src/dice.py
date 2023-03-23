class Dice:

    import random

    def __init__(self):
        self.die1 = 0
        self.die2 = 0
        self.die3 = 0

    def std_roll(self):
        """
        Simulate rolling two standard six-sided dice.
        """
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        return [self.die1, self.die2]

    def spec_roll(self):
        """
        Simulate rolling one user defined six-sided dice.
        """
        num_lst = [2, 4, 8, 16, 32, 64]
        self.die3 = random.choice(num_lst)
        return self.die3
