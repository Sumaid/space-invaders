class Missiles:

    def __init__(self):
        pass

    def mgposit(self):
        return self.position


class Smissile(Missiles):

    def __init__(self, shipposition):
        self.symbol = 'i'
        self.nsymbol = ' '
        self.position = shipposition-9
        Missiles.__init__(self)

    def uposit(self):
        if self.position > 18:
            self.position -= 9

    def nposit(self):
        return self.position-9


class Fmissile(Missiles):

    def __init__(self, shipposition):
        self.symbol = 'l'
        self.nsymbol = '%'
        self.position = shipposition - 9
        Missiles.__init__(self)

    def uposit(self):
        if self.position > 27:
            self.position -= 18

    def nposit(self):
        return self.position-18

