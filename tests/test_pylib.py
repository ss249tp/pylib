import pylib


def test_true():
    assert pylib.true()
    assert pylib.true(0)
    assert pylib.true("123")
