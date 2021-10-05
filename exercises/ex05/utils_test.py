"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730307980"


def test_all_evens() -> None:
    """A Test for a list of all evens"""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_empty() -> None:
    """A Test for an empty list"""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_usage() -> None:
    """A Test for a full list"""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_start_neg() -> None:
    """A Test for a negative start index"""
    xs: list[int] = [1, 2, 3, 4]
    a: int = -7
    b: int = 3
    assert sub(xs, a, b) == [1, 2, 3]


def test_full_list() -> None:
    """A Test that should return a full list"""
    xs: list[int] = [1, 2, 3, 4]
    a: int = -7
    b: int = 10
    assert sub(xs, a, b) == [1, 2, 3, 4]
    

def test_list_normal() -> None:
    """A Test that should return a subset of a list"""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = 2
    b = 8
    assert sub(xs, a, b) == [3, 4, 5, 6, 7, 8]


def test_empty_lists() -> None:
    """A Test that should return an empty list"""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_regular_use() -> None:
    """A Test that should return the concatanation of 2 lists"""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_repeated_list() -> None:
    a: list[int] = [1, 3, 4]
    assert concat(a, a) == [1, 3, 4, 1, 3, 4]
