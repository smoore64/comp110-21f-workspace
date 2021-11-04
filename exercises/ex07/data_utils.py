"""Utility functions."""

__author__ = "730307980"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads CSV into row based form."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    
    file_handle.close()
    return result


def column_values(tab: list[dict[str, str]], col: str) -> list[str]:
    """Shows values in a column."""
    vals: list[str] = []
    for item in tab:
        vals.append(item[col])
    return vals


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Switches to column-based."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = rows[0]
    for col in first_row:
        result[col] = column_values(rows, col)
    return result


def head(tab: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Displays only certain rows."""
    result: dict[str, list[str]] = {}
    if rows < len(tab):
        for col in tab:
            i: int = 0
            items: list[str] = []
            while i < rows:
                items.append(tab[col][i])
                i += 1
            result[col] = items
    else:
        result = tab
    return result


def select(tab: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Selects columns."""
    result: dict[str, list[str]] = {}
    for name in cols:
        result[name] = tab[name]
    return result


def concat(tab1: dict[str, list[str]], tab2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine 2 column based tables."""
    result: dict[str, list[str]] = {}
    for key in tab1:
        result[key] = tab1[key]
    for key in tab2:
        if key in result:
            for item in tab2[key]:
                result[key].append(item)
        else:
            result[key] = tab2[key]
    return result


def count(vals: list[str]) -> dict[str, int]:
    """Counts occurance of value."""
    result: dict[str, int] = {}
    for item in vals:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
