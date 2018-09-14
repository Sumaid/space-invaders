import random


class Aliens:

    def __init__(self, birthtime):
        self.symbol = '@'
        self.birthtime = birthtime
        self.position = random.randint(10, 26)
        while self.position == 18:
            self.position = random.randint(10, 26)

    def checker(self, curtime):
        if (curtime == self.birthtime+8):
            return True
        else:
            return False

    def agposit(self):
        return self.position

