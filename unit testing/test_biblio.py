from biblio import Biblio
import pytest

b = [('My Life','Terry'),("Terry's Life",'Janet'),("Terry 2: the Return",'Janet')]

@pytest.fixture
def biblio():
    return Biblio(b)

def test_ajouterlivre(biblio):
    book=("Terry's Detailed Biography",'Janet')
    assert book not in biblio.listerlivres()
    biblio.ajouterlivre(*book)
    assert book in biblio.listerlivres()

def test_generationstat(biblio):
    stats = biblio.generationstat()
    # assert n == len(biblio.listerlivres())
    # assert ars == {'Terry','Janet'}
    assert stats == {
        'nombre_livres': 3,
        'auteurs_uniques': {'Terry', 'Janet'},
    }

def test_supprimerlivre(biblio):
    assert ("Terry's Life",'Janet') in biblio.listerlivres()
    biblio.supprimerlivre("Terry's Life")
    assert ("Terry's Life",'Janet') not in biblio.listerlivres()


def test_rechercherlivreauteur(biblio):
    ls = biblio.rechercherlivreauteur('Janet')
    assert len(ls) > 0
    for l in ls:
        assert l[1]=='Janet'

    ls = biblio.rechercherlivreauteur('Terry')
    assert len(ls) > 0
    for l in ls:
        assert l[1]=='Terry'

def test_listerlivres(biblio):
    assert biblio.listerlivres() == b
    assert biblio.listerlivres() == [('My Life','Terry'),("Terry's Life",'Janet'),("Terry 2: the Return",'Janet')]
