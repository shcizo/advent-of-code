"""Input parsing and common utilities for Advent of Code."""

from pathlib import Path
from typing import Callable, Any
import numpy as np


def get_input_path(day: int) -> Path:
    """Get the path to input file for a given day."""
    return Path(__file__).parent.parent / "inputs" / f"day{day:02d}.txt"


def read_input(day: int) -> str:
    """Read raw input for a given day."""
    return get_input_path(day).read_text().strip()

def read_lines_and_split(day: int, split: str) -> list:
    """Read input as lines, optionally parsing each line."""
    return [line for line in read_input(day).split(split)]

def read_lines(day: int, parser: Callable[[str], Any] = str) -> list:
    """Read input as lines, optionally parsing each line."""
    return [parser(line) for line in read_input(day).splitlines()]


def read_ints(day: int) -> list[int]:
    """Read input as list of integers (one per line)."""
    return read_lines(day, int)


def read_grid(day: int, dtype=str, split=False, keep_spaces=False, width=None):
    """Read input as a 2D grid.

    split=False: each character is a cell (default)
    split=True:  split on whitespace
    split=',':   split on specific delimiter
    keep_spaces: preserve all whitespace (don't strip)
    width=5:     fixed-width columns (5 chars each)
    """
    if width:
        lines = get_input_path(day).read_text().splitlines()
        rows = []
        for line in lines:
            row = [line[i:i+width].strip() for i in range(0, len(line), width)]
            rows.append(row)
        return np.array(rows)
    if keep_spaces:
        lines = get_input_path(day).read_text().splitlines()
        max_len = max(len(line) for line in lines)
        rows = [list(line.ljust(max_len)) for line in lines]
        return rows
    lines = read_input(day).splitlines()
    if split:
        delim = None if split is True else split
        rows = [line.split(delim) for line in lines]
        if dtype == int:
            return np.array([[int(x) for x in row] for row in rows])
        return np.array(rows)
    if dtype == int:
        return np.array([[int(c) for c in line] for line in lines])
    return np.array([list(line) for line in lines])


def read_blocks(day: int) -> list[str]:
    """Read input split by blank lines (paragraphs)."""
    return read_input(day).split("\n\n")


def to_digit_grids(grid):
    """Convert whitespace-split grid to list of digit grids.

    Input:  [['123', '328'], ['45', '64'], ['6', '98']]
    Output: [
        [['1','2','3'], ['4','5',''], ['6','','']],  # kolumn 1
        [['3','2','8'], ['6','4',''], ['9','8','']]  # kolumn 2
    ]
    """
    cols = list(zip(*grid))
    grids = []
    for col in cols:
        max_len = max(len(s) for s in col)
        digit_grid = [[c for c in s] + [''] * (max_len - len(s)) for s in col]
        grids.append(np.array(digit_grid))
    return grids


def split_grid_on_cols(grid):
    """Split grid on whitespace columns.

    Input: grid from read_grid(day, keep_spaces=True)
    Returns: list of numpy arrays, one per column group
    """
    arr = np.array(grid)
    empty_cols = np.all(arr == ' ', axis=0)

    # Hitta start/slut för varje grupp (icke-tomma kolumner)
    result = []
    in_group = False
    start = 0

    for i, is_empty in enumerate(empty_cols):
        if not is_empty and not in_group:
            start = i
            in_group = True
        elif is_empty and in_group:
            result.append(arr[:, start:i])
            in_group = False

    # Sista gruppen
    if in_group:
        result.append(arr[:, start:])

    return result


# Common grid directions
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
DIRS_8 = DIRS_4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # + diagonals

# Direction mappings
DIR_MAP = {
    "R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0),
    ">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0),
}
