"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730307980"


def test_key_1() -> None:
    """Regular list invert."""
    a: dict[str, str] = {"a": "b", "c": "j", "d": "e"}
    assert invert(a) == {"b": "a", "j": "c", "e": "d"}


def test_normal_list() -> None:
    """Normal list invert."""
    a: dict[str, str] = {"a": "b", "c": "f", "d": "e"}
    assert invert(a) == {"b": "a", "f": "c", "e": "d"}


def test_empty_dict() -> None:
    """Empty dict."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_favorite1() -> None:
    """Normal dict favorite test."""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_uniform() -> None:
    """Everyone has the same!"""
    a: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_color_caps() -> None:
    """Some capitalization issues."""
    a: dict[str, str] = {"Marc": "Blue", "Ezri": "blue", "Kris": "bLue"}
    assert favorite_color(a) == "Blue"


def test_count_1() -> None:
    """List with 1 value."""
    a: list[str] = ["Tottenham"]
    assert count(a) == {"Tottenham": 1}


def test_count_threediff() -> None:
    """List with 3 different value."""
    a: list[str] = ["Tottenham", "Arsenal", "Man U", "Tottenham", "Arsenal", "Man U"]
    assert count(a) == {"Tottenham": 2, "Arsenal": 2, "Man U": 2}


def test_count_threesame() -> None:
    """List with 3 of the same value."""
    a: list[str] = ["Tottenham", "Tottenham", "Tottenham"]
    assert count(a) == {"Tottenham": 3}