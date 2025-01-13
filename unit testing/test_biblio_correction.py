import bibliotheque

def test_ajouter_livre():
    lib = bibliotheque.Bibliotheque()
    lib.ajouter_livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
    assert lib.lister_livres() == [("Le Seigneur des Anneaux", "J.R.R. Tolkien")]

def test_supprimer_livre():
    lib = bibliotheque.Bibliotheque()
    lib.ajouter_livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
    lib.supprimer_livre("Le Seigneur des Anneaux")
    assert lib.lister_livres() == []

def test_rechercher_livres_par_auteur():
    lib = bibliotheque.Bibliotheque()
    lib.ajouter_livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
    lib.ajouter_livre("Harry Potter", "J.K. Rowling")
    livres = lib.rechercher_livres_par_auteur("J.R.R. Tolkien")
    assert livres == [("Le Seigneur des Anneaux", "J.R.R. Tolkien")]

def test_statistiques_bibliotheque():
    lib = bibliotheque.Bibliotheque()
    lib.ajouter_livre("Le Seigneur des Anneaux", "J.R.R. Tolkien")
    lib.ajouter_livre("Harry Potter", "J.K. Rowling")
    stats = lib.generer_statistiques()
    assert stats == {
        'nombre_livres': 2,
        'auteurs_uniques': {'J.R.R. Tolkien', 'J.K. Rowling'},
    }
