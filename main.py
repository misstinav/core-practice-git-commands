import pytest

print("this is our collaboration test")

def always_returns_true():
    return True


def test_always_returns_true():
    assert always_returns_true()
