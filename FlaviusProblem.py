# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Pile as pile


class Flavius:

    def __init__(self):
        self.pile = pile.Pile()
        self.reversePile = pile.Pile()
        for i in range(41, 0, -1):
            self.pile.empiler(i)
        print(str(self.pile))

    def oneTurn(self):
        count = 1
        self.pile.depiler()
        while not self.pile.estPileVide():
            if count % 3 != 0 or count == 0:
                self.reversePile.empiler(self.pile.depiler())
            else:
                self.pile.depiler()
            count += 1
        self.reversingPile()

    def reversingPile(self):
        while not self.reversePile.estPileVide():
            self.pile.empiler(self.reversePile.depiler())

    def game(self):
        while len(self.pile.pile) != 1:
            self.oneTurn()
            print(self.pile)
        print("end")


Flavius().game()
