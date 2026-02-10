from test import add

def test_add_positive():
    assert add(2, 3)


def test_add_negative():
    assert add(-4, -2)

def test_add_mixed():
    assert add(-2, 1)