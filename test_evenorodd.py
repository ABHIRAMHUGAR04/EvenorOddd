from evenorodd import even_odd
def test_even_odd():
    assert even_odd(4) == "Even"

def test_even_odd_odd():
    assert even_odd(5) == "Odd"