from mylib.soccer import Player, PlayerPhysicalAttributes

def test_player():
    p = Player('John', 10, 'Forward')
    assert p.name == 'John'
    assert p.number == 10
    assert p.position == 'Forward'

def test_player_physical_attributes():
    p = PlayerPhysicalAttributes('John', 10, 'Forward')
    assert p.weight == 65