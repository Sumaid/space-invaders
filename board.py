import os


class Board:

    def __init__(self):
        self.blocks = [' '] * 81
        self.score = 0

    def update(self, pos, marker):
        self.blocks[pos] = marker

    def update2(self, pos, pos1, marker, marker1):
        self.blocks[pos] = marker
        self.blocks[pos1] = marker1

    def scoreup(self):
        self.score += 1

    def gprint(self):
        os.system('clear')
        for i in range(9):
            for j in range(9):
                print self.blocks[i*9+j],
            print
        print "Score:", self.score

