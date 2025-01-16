import tri

def test_tri_croissant():
    assert tri.trier([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_tri_decroissant():
    assert tri.trier([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], croissant=False) == [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
