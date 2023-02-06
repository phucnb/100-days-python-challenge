from main import calculate


def test_calculate():
    assert calculate(2.0, "/", 3.0) == 2.0 / 3.0
    assert calculate(2.0, "+", 3.0) == 2.0 + 3.0
    assert calculate(2.0, "-", 3.0) == 2.0 - 3.0
    assert calculate(2.0, "*", 3.0) == 2.0 * 3.0