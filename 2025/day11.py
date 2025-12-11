"""Day 11: Advent of Code 2025."""

import time
from collections import defaultdict
from aoc import read_lines


def build_graph(data: list[str]) -> dict[str, set[str]]:
    """Build graph from input: 'fxp: udl vii hgb qmy' -> adjacency dict."""
    graph = defaultdict(set)
    for line in data:
        node, neighbors = line.split(': ')
        for neighbor in neighbors.split():
            graph[node].add(neighbor)
            
    return graph

def count_paths(node, target, graph, memo={}):
      if node == target:
          return 1
      if node in memo:
          return memo[node]

      total = 0
      for neighbor in graph[node]:
          total += count_paths(neighbor, target, graph, memo)

      memo[node] = total
      return total

def part1(data):
    """Solve part 1."""
    graph = build_graph(data)
    count = count_paths("you", "out", graph)
    return count


def part2(data):
    """Solve part 2."""
    graph = build_graph(data)
    c1 = count_paths("svr", "dac", graph, {})
    c2 = count_paths("dac", "fft", graph, {})
    c3 = count_paths("fft", "out", graph, {})
    c4 = count_paths("svr", "fft", graph, {})
    c5 = count_paths("fft", "dac", graph, {})
    c6 = count_paths("dac", "out", graph, {})

    return (c1 * c2* c3) + (c4*c5*c6)


if __name__ == "__main__":
    DAY = 11
    data = read_lines(DAY)

    t0 = time.perf_counter()
    p1 = part1(data)
    t1 = time.perf_counter()
    print(f"Part 1: {p1}  ({(t1-t0)*1000:.2f} ms)")

    t0 = time.perf_counter()
    p2 = part2(data)
    t1 = time.perf_counter()
    print(f"Part 2: {p2}  ({(t1-t0)*1000:.2f} ms)")
