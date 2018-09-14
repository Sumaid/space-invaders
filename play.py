import os
import time
import random
import time
import threading
import math
from pynput import keyboard
from aliens import *
from board import *
from ship import *
from missiles import *


class engine:

    def __init__(self):
        self.curtime = int(math.floor(time.time()))
        self.start = self.curtime
        self.aliensdict = {}
        self.missilesdict = []
        self.newb = Board()
        self.newsh = Ship()

    def initializer(self):
        k = 8
        for i in range(1, 9):
            self.newb.update(i*9, k)
            k -= 1
        for i in range(1, 9):
            self.newb.update(i, i)
        self.newb.update(self.newsh.sgposit(), self.newsh.symbol)

    def timelord(self):
        while (1):
            self.curtime = int(math.floor(time.time()-self.start))
            if self.curtime % 10 == 0:
                temp = Aliens(self.curtime)
                self.aliensdict[temp.agposit()] = temp
                self.newb.update(temp.agposit(), '@')
            for item in self.aliensdict.values():
                if (item.checker(self.curtime)):
                    self.newb.update(item.agposit(), ' ')
                    self.aliensdict.pop(item.agposit(), None)
            for item in self.missilesdict:
                if item.__class__ == Fmissile and \
                   item.nposit() in self.aliensdict.keys():
                    self.newb.scoreup()
                    self.aliensdict[item.nposit()].birthtime = self.curtime-3
                    self.newb.update2(item.mgposit(), item.nposit(), ' ', '%')
                    self.missilesdict.remove(item)
                elif item.__class__ == Smissile and \
                        item.nposit() in self.aliensdict.keys():
                    self.newb.scoreup()
                    self.newb.update2(item.mgposit(), item.nposit(), ' ', ' ')
                    self.aliensdict.pop(item.mgposit()-9, None)
                    self.missilesdict.remove(item)
                elif item.mgposit() in range(10, 18):
                    self.newb.update(item.mgposit(), ' ')
                else:
                    self.newb.update2(
                        item.mgposit(), item.nposit(), ' ', item.symbol)
                    item.uposit()
            self.newb.gprint()
            time.sleep(1)

    def shipmover(self, ch):
        oldposition = self.newsh.sgposit()
        self.newsh.uposit(ch)
        self.newb.update2(oldposition, self.newsh.sgposit(),
                          ' ', self.newsh.symbol)
        self.newb.gprint()

    def launcher(self, ch):
        if ch == 'fast':
            self.missilesdict.append(Fmissile(self.newsh.sgposit()))
        elif ch == 'slow':
            self.missilesdict.append(Smissile(self.newsh.sgposit()))
        self.newb.update(self.newsh.sgposit()-9, self.missilesdict[-1].symbol)
        self.newb.gprint()

    def keychecker(self, ch):
        if ch == 'q':
            os.system('clear')
            self.newb.gprint()
            exit()
        elif ch == 's':
            self.launcher('fast')
            return
        elif ch == 'a' or ch == 'd':
            self.shipmover(ch)
        else:
            print "Invalid Key"

    def runner(self):
        self.initializer()
        thr = threading.Thread(target=self.timelord, args=(), kwargs={})
        thr.daemon = True
        thr.start()

        def on_press(key):
            if hasattr(key, 'char'):
                self.keychecker(key.char)
            else:
                if key._name_ == "space":
                    self.launcher('slow')
                else:
                    print "Invalid Key"

        with keyboard.Listener(
                on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    e = engine()
    e.runner()

