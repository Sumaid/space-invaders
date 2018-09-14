from random import *


class Ship:

    def __init__(self):
        self.symbol = '$'
        self.position = randint(73, 80)

    def uposit(self, char):
        if char == 'a':
            if self.position > 73:
                self.position -= 1
        if char == 'd':
            if self.position < 80:
                self.position += 1

    def sgposit(self):
        return self.position

