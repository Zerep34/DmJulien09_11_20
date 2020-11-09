class Pile:
    """
    Attributs :
        pile : tableau dynamique Python
    Méthodes:
        __init()__ constructeur de la classe
        estPileVide() : renvoie un booléen Vrai sssi la pile est vide
        empiler(élément) : empile élément au sommet de la pile
        depiler() : si la pile est vide, renvoie une erreur
                    sinon, renvoie l'élément au sommet de la pile et le supprime
        sommet() : si la pile est vide, renvoie une erreur
                    sinon, renvoie l'élément au sommet de la pile sans le supprimer
    """

    def __init__(self):
        self.pile = []

    def estPileVide(self):
        return self.pile == []

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        if self.estPileVide():
            raise IndexError("la pile est vide")
        else:
            return self.pile.pop()

    def sommet(self):
        if self.estPileVide():
            raise IndexError("la pile est vide")
        else:
            return self.pile[-1]

    def __repr__(self):
        if self.estPileVide():
            return 'Pile vide'
        else:
            return str(self.pile)