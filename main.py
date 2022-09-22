import pytest


def always_returns_true():
    return "Collab problem"


def test_always_returns_true():
    assert always_returns_true()
