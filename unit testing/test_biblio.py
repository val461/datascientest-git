from biblio import Biblio

b = [('My Life','Terry'),("Terry's Life",'Janet')]

@pytest.fixture
def biblio():
    return Biblio(b)

def test_ajouterlivre(biblio):
    book=("Terry's Detailed Biography",'Janet')
    assert book not in biblio.listerlivres()
    biblio.ajouterlivre(book)
    assert book in biblio.listerlivres()

def test_generationstat(biblio):
    n,ars = generationstat()
    assert n == len(biblio.listerlivres())
    assert ars == len(biblio.listerlivres())

def test_supprimerlivre(biblio):
    assert ('My Life','Terry') in biblio.listerlivres()
    biblio.supprimerlivre('My Life')
    assert ('My Life','Terry') not in biblio.listerlivres()


def test_rechercherlivreauteur(biblio):
    ls = biblio.rechercherlivreauteur('Janet')
    assert len(ls) > 0
    for l in ls:
        assert l[1]=='Janet'


def test_listerlivres(biblio):
    assert biblio.listerlivres == b
    assert biblio.listerlivres == [('My Life','Terry'),("Terry's Life",'Janet')]
