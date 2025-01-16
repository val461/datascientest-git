class Biblio:
    def __init__(self,b=None):
        self.b = [] if b is None else list(b)

    def ajouterlivre(self,titre,auteur):
        self.b.append((titre,auteur))

    def supprimerlivre(self,titre):
        self.b = [(t,a) for t,a in self.b if t != titre]

    def listerlivres(self):
        return list(self.b)

    def rechercherlivreauteur(self,auteur):
        return [(t,a) for t,a in self.b if a == auteur]

    def generationstat(self):
        return {
            'nombre_livres': len(self.b),
            'auteurs_uniques': {a for t,a in self.b},
        }
