"""Day 10: Advent of Code 2025."""

import time
import re
from aoc import read_lines
from itertools import combinations, product
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


def parse_targets(s: str) -> list[int]:
    """Parse {28,20,8,20} -> [28, 20, 8, 20] (target values per position)."""
    match = re.search(r'\{([^}]+)\}', s)
    if not match:
        return []
    return [int(x) for x in match.group(1).split(',')]


def parse_total(s: str) -> int:
    """Parse [.##.] -> 0b0110 (binary representation)."""
    match = re.search(r'\[([.#]+)\]', s)
    if not match:
        return 0
    pattern = match.group(1)
    return int(pattern.replace('.', '0').replace('#', '1'), 2)


def parse_groups_as_positions(s: str) -> list[list[int]]:
    """Parse (3) (1,3) (2) -> [[3], [1,3], [2], ...].

    Returns list of groups, where each group is a list of positions it affects.
    """
    groups = re.findall(r'\(([^)]+)\)', s)
    result = []
    for group in groups:
        positions = [int(x) for x in group.split(',')]
        result.append(positions)
    return result


def build_matrix(groups: list[list[int]], width: int) -> list[list[int]]:
    """Build matrix where matrix[pos][group] = 1 if group affects position pos.

    Rows = positions (0 to width-1)
    Columns = groups
    """
    matrix = []
    for pos in range(width):
        row = []
        for group in groups:
            row.append(1 if pos in group else 0)
        matrix.append(row)
    return matrix


def solve_system(matrix: list[list[int]], targets: list[int]) -> int | None:
    """Solve the system and find minimum sum of k values.

    Uses Mixed Integer Linear Programming:
    - Minimize: sum of all k values
    - Subject to: matrix @ k = targets, k >= 0, k are integers

    Returns minimum sum of k values, or None if no solution.
    """
    if not matrix or not matrix[0]:
        return None

    num_groups = len(matrix[0])

    # Convert to numpy arrays
    A_eq = np.array(matrix, dtype=float)
    b_eq = np.array(targets, dtype=float)

    # Objective: minimize sum of k (coefficients all 1)
    c = np.ones(num_groups)

    # Bounds: k >= 0 (upper bound = max target value is safe)
    max_val = max(targets) + 1
    bounds = Bounds(lb=np.zeros(num_groups), ub=np.full(num_groups, max_val))

    # Equality constraints: A @ k = b
    constraints = LinearConstraint(A_eq, b_eq, b_eq)

    # All variables must be integers
    integrality = np.ones(num_groups)  # 1 = integer

    # Solve
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)

    if not result.success:
        return None

    return int(round(result.fun))


def parse_groups(s: str, width: int) -> list[list[int]]:
    """Parse (3) (1,3) (2) -> [[bitmask, inverse], ...].

    (1,3) with width 4 -> positions 1 and 3 from left -> 0101 (decimal 5)
    Then also the inverse -> 1010 (decimal 10)
    """
    groups = re.findall(r'\(([^)]+)\)', s)
    result = []
    mask_all = (1 << width) - 1  # All bits set for inverse calculation

    for group in groups:
        nums = [int(x) for x in group.split(',')]
        # Combine all positions into one bitmask (from left, so invert position)
        bitmask = 0
        for n in nums:
            # Position n from left = bit (width - 1 - n) from right
            bitmask |= (1 << (width - 1 - n))
        # Duplicate the bitmask (using same value twice XORs to 0)
        result.append([bitmask, bitmask])

    return result


def parse_line(line: str) -> tuple[int, list[list[int]]]:
    """Parse full line, return (total_bitmask, groups)."""
    # Get width from the [...] pattern
    match = re.search(r'\[([.#]+)\]', line)
    width = len(match.group(1)) if match else 0

    total = parse_total(line)
    groups = parse_groups(line, width)
    return total, groups


def combine_bitmasks(*bitmasks: int) -> int:
    """Combine bitmasks with XOR."""
    result = 0
    for b in bitmasks:
        result ^= b
    return result

def find_min_index_sum(total: int, groups: list[list[int]]) -> int:
    """Find minimum index sum for combos that XOR to total.

    Tries subsets of groups starting from smallest (r=1, r=2, ...).
    Within each r, minimum possible sum is r (all index 0 -> r * 1).
    If we find a match with sum S, we can skip any r where r > S.
    """
    n = len(groups)
    # Max possible sum: n groups * 2 (max index 1 -> +2 each)
    best = n * 2 + 1

    for r in range(1, n + 1):
        # Minimum possible sum for r groups is r (all index 0 = 1 each)
        if r >= best:
            break

        for group_indices in combinations(range(n), r):
            selected_groups = [groups[i] for i in group_indices]

            # Try all index combinations within selected groups
            for indices in product(*[range(len(g)) for g in selected_groups]):
                index_sum = sum(idx + 1 for idx in indices)

                # Skip if can't beat best
                if index_sum >= best:
                    continue

                bitmasks = [selected_groups[i][idx] for i, idx in enumerate(indices)]
                if combine_bitmasks(*bitmasks) == total:
                    best = index_sum

    return best


def part1(data):
    result = 0
    for line in data:
        total, groups = parse_line(line)
        result += find_min_index_sum(total, groups)
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    for line in data:
        groups = parse_groups_as_positions(line)
        targets = parse_targets(line)
        width = len(targets)
        matrix = build_matrix(groups, width)
        result += solve_system(matrix, targets)
    return result


if __name__ == "__main__":
    DAY = 10  # <- ändra till rätt dag
    data = read_lines(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
