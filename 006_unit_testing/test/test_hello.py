from hello import hello


def test_default_value():
    hello() == "hello, world"


def test_argument():
    hello("David") == "hello, David"
