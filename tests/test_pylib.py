import pylib


def test_true():
    assert pylib.true()
    assert pylib.true(0)
    assert pylib.true("123")


def test_false():
    assert not pylib.false()
    assert not pylib.false(0)
    assert not pylib.false("123")
