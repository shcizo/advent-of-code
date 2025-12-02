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


def read_grid(day: int, dtype=str) -> np.ndarray:
    """Read input as a 2D numpy grid of characters or digits."""
    lines = read_input(day).splitlines()
    if dtype == int:
        return np.array([[int(c) for c in line] for line in lines])
    return np.array([list(line) for line in lines])


def read_blocks(day: int) -> list[str]:
    """Read input split by blank lines (paragraphs)."""
    return read_input(day).split("\n\n")


# Common grid directions
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
DIRS_8 = DIRS_4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # + diagonals

# Direction mappings
DIR_MAP = {
    "R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0),
    ">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0),
}
